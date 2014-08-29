from mongoengine.base import BaseField
from Crypto.Cipher import AES
from exceptions import EncryptionKeyException
import binascii

class EncryptedField(BaseField):
    
    ''' Constants '''

    AES = 'AES'
    SHA_256 ='SHA256' # Hashing algorithm
    AES_SHA='AES+SHA'

    ''' Attributes '''

    prefix = '@::::@' # Prefix that values will have
    algorithm = AES # Default algorithm value
    internal_type = None # Internal type of the encrypted value
    

    def __init__(self, algorithm=None, key=None,iv=None,**kwargs):
        if algorithm:
            self.algorithm = algorithm
        self.key = key
        self.iv = iv
        super(EncryptedField, self).__init__(**kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self

        value=instance._data.get(self.name)

        if (value.startswith(self.prefix)):
            value=self.decrypt_value(value)      
        
        return value

    def __set__(self, instance, value):
        value = str(value)
        if (not value.startswith(self.prefix)):
            value = self.encrypt_value(value)
        super(EncryptedField, self).__set__(instance, value)

    def to_mongo(self,value):
        return str(value)

    def prepare_query_value(self, op, value):        
        return self.encrypt_value(value)

    def get_internal_type(self):
        return self.internal_type

    ''' AES Functions '''

    def get_aes_cipher(self):
        if len(self.key)==16 or len(self.key)==24 or len(self.key)==32:
            if self.iv and len(self.iv)==16:
                return AES.new(self.key,IV=self.iv)
            else:
                return AES.new(self.key)
        else:
            raise EncryptionKeyException()

    def aes_decryption(self,value):
        cipher = self.get_aes_cipher()
        return cipher.decrypt(binascii.unhexlify(value)).rstrip()

    def aes_encryption(self,value):
        cipher = self.get_aes_cipher()
        # The value must be a multiple of 16
        value=value + (" " * (16 - (len(value) % 16)))
        return binascii.hexlify(cipher.encrypt(value))

    ''' General Encryption Functions '''

    def decrypt_value (self,value):
        if (value.startswith(self.prefix)):
            if self.algorithm == self.AES:

                # First it removes the prefix
                value = self.aes_decryption(value[len(self.prefix):])
        return value

    def encrypt_value(self,value):
        if self.algorithm == self.AES:
            value = self.aes_encryption(value)

            # Adds a prefix, so it is possible to know, at __set__ time, if the value is encrypted
            value = self.prefix + value
        return value
