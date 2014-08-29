Welcome to SecureMongoEngine
=============================================

It is a library for MongoEngine(https://github.com/MongoEngine) that you can use to encrypt certain fields of your models. Currently is in Beta Version and it only supports AES for Symmetric Encryption and SHA for hashing.

Usage
-------

If you want to encrypt your data you only need to use the field that you need. ::

	from mongoengine import *
	from securemongoengine.fields import *

	_key = 'workingWithAES256AlgorithmKey32B'

	class User(Document):
	    name = EncryptedStringField(key=_key,max_length=40, required=True)
	    lastname = EncryptedStringField(key=_key,max_length=40, required=True)
	    email = EncryptedEmailField(key=_key,required=True, unique=True)
	    password = EncryptedStringField(key=_key,max_length=40, required=True)
	    phone_number = EncryptedLongField(key=_key,min_value=8, max_value=99999999999)
	    money = EncryptedDecimalField(key=_key)
	    age = EncryptedIntField(key=_key)
	    height = EncryptedFloatField(key=_key,required=False)

	    meta = {'allow_inheritance': True, 'collection':'users'}

	user = User(name='Juan',lastname='Urrego',email='js.urrego@novcat.co',password = '123456', phone_number=11234567,money=243.23,age=26,height=1.75)

	user.save()

	print User.objects().first().to_mongo()

	>> SON([('_id', ObjectId('53ffe57f5f9370cbd8a2bea6')), ('_cls', 'User'), ('name', '@::::@d641ab1294

Contents:

.. toctree::
   :maxdepth: 2

:doc:`tutorial`
  A quick tutorial building a tumblelog to get you up and running with
  SecureMongoEngine.


:doc:`apireference`
  The complete API documentation



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`