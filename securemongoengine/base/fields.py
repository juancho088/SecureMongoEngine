from mongoengine.base import BaseField
from Crypto.Cipher import AES
from exceptions import EncryptionKeyException, CipherModeException
import binascii

class EncryptedField(BaseField):
    
    ''' Constants '''

    _AES = 'AES'
    _SHA_256 ='SHA256' # Hashing algorithm
    _AES_SHA='AES+SHA'

    _CBC = 'CBC'
    _CFB = 'CFB'
    _CTR = 'CTR'
    _OFB = 'OFB'
    _OPENPGP = 'OPENPGP'

    ''' Attributes '''

    algorithm = _AES # Default algorithm value
    internal_type = None # Internal type of the encrypted value
    mode = AES.MODE_CBC
    
    def __init__(self, algorithm=None, key=None,iv=None,mode=None,**kwargs):
        if algorithm:
            self.algorithm = algorithm

        if mode:
            if mode== self._CBC:
                self.mode = AES.MODE_CBC
            elif mode== self._CFB:
                self.mode = AES.MODE_CFB
            elif mode==self._CTR:
                self.mode = AES.MODE_CTR
            elif mode== self._OFB:
                self.mode = AES.MODE_OFB
            elif mode== self._OPENPGP:
                self.mode = AES.MODE_OPENPGP
            else:
                raise CipherModeException()

        self.key = key
        self.iv = iv
        super(EncryptedField, self).__init__(**kwargs)

    def __set__(self, instance, value):
        try:
            value=self.decrypt_value(value)
        except:
            pass #In case that the value is not encrypted (after decryption for example) 
        super(EncryptedField, self).__set__(instance, value)

    def to_mongo(self,value):
        return self.encrypt_value(str(value))

    def prepare_query_value(self, op, value):        
        return self.encrypt_value(value)

    def get_internal_type(self):
        return self.internal_type

    ''' AES Functions '''

    def get_aes_cipher(self):
        if len(self.key)==16 or len(self.key)==24 or len(self.key)==32:
            if self.iv and len(self.iv)==16:
                return AES.new(self.key,IV=self.iv,mode=self.mode)
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
        if self.algorithm == self._AES:
            # First it removes the prefix
            value = self.aes_decryption(value)
        return value

    def encrypt_value(self,value):
        if self.algorithm == self._AES:
            value = self.aes_encryption(value)

            # Adds a prefix, so it is possible to know, at __set__ time, if the value is encrypted
            value = value
        return value
