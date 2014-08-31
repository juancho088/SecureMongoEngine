SecureMongoEngine
=================

It is a library for MongoEngine https://github.com/MongoEngine/mongoengine that you can use to encrypt certain fields of your models. Currently is in Beta Version and it only supports AES for Symmetric Encryption and SHA for hashing.

Usage
-------

To install SecureMongoeEngine, just execute:

	$ pip install securemongoengine

And now you can create a documment with some encrypted fields, you just need a key an thats all!!:
	
	from mongoengine import *
	from securemongoengine.fields import *

	_key = 'workingWithAES256AlgorithmKey32B'

	class User(Document):
	    name = StringField(max_length=40, required=True)
	    lastname = StringField(max_length=40, required=True)
	    email = EmailField(required=True, unique=True)
	    password = EncryptedStringField(key=_key,max_length=40, required=True)
	    
	user = User(name='Juan',lastname='Urrego',email='js.urrego@novcat.co',password = '123456')

	connect('test', host='127.0.0.1')
	user.save()

In your Mongo database you will see something like this:

	{ "_id" : ObjectId("5400c7205f9370f0603c3cfa"), "name" : "Juan", "lastname" : "Urrego", 
	"email" : "js.urrego@novcat.co", "password" : "685f0500d7b99a59c9d6c496184a65bc" }
	
Documentation
-------------

The complete documentation of the project can be found in http://securemongoengine.readthedocs.org
