from mongoengine import *
from securemongoengine.fields import *
import random

_key = 'workingWithAES256AlgorithmKey32B'

class User(Document):
    name = EncryptedStringField(key=_key,max_length=40, required=True,mode='EBC',iv=''.join(chr(random.randint(0, 0xFF)) for i in range(16)))
    lastname = EncryptedStringField(key=_key,max_length=40, required=True)
    email = EncryptedEmailField(algorithm='AES',key=_key,required=True, unique=True)
    password = EncryptedStringField(key=_key,max_length=40, required=True)
    phone_number = EncryptedLongField(key=_key,min_value=8, max_value=99999999999)
    money = EncryptedDecimalField(algorithm='AES',key=_key)
    age = EncryptedIntField(algorithm='AES',key=_key)
    height = EncryptedFloatField(key=_key,required=False)

    meta = {'allow_inheritance': True, 'collection':'users'}
