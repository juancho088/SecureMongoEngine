========
Tutorial
========

Here we will introduce the main features of SecureMongoEngine, and how to use it in a real environment.

Installation
===============

SecureMongoEngine uses `MongoEngine <https://github.com/MongoEngine/mongoengine>`_ and `pyCrypto <https://github.com/dlitz/pycrypto>`_, so it is able to encrypt all the data that you need. It is available on PyPI, so to use it you can use pip: ::

	$ pip install securemongoengine

Or you can also use easy_install: ::

	$ easy_install securemongoengine

Alternatively, if you don’t have setuptools installed, download it from PyPi or Github and run: ::

	$ python setup.py install

Encrypted Fields
======================

The main idea of SecureMongoEngine is that you can transparently use encryption using MongoEngine models. By default all the fields will encrypt your data with AES, nevertheless you can change the encryption algorithm. The library has differents fields, so even when the data is encrypted you will see the plain values in python. Next we will present the differents fields:

* :class:`~securemongoengine.fields.EncryptedEmailField`
* :class:`~securemongoengine.fields.EncryptedStringField`
* :class:`~securemongoengine.fields.EncryptedIntField`
* :class:`~securemongoengine.fields.EncryptedDecimalField`
* :class:`~securemongoengine.fields.EncryptedFloatField`
* :class:`~securemongoengine.fields.EncryptedLongField`

Field arguments
----------------

Each field type can be customized by keyword arguments. The following keyword arguments can be set on all fields: 

:attr:`algorithm` **(Default: 'AES')**
	Defines which encryption algorithm is going to be used. By default, SecureMongoEngine uses AES and the size of the encryption key will define if it will AES256, AES192 or AES128. More details next.

:attr:`key` **(Default: None)**
	Is the value needed to make the encryption. The key size used for an AES cipher specifies the number of repetitions of transformation rounds that convert the input, called the plaintext, into the final output, called the ciphertext. The number of cycles of repetition will be:

	* 10 cycles of repetition for 128-bit (16 Bytes) keys.
	* 12 cycles of repetition for 192-bit (24 Bytes) keys.
	* 14 cycles of repetition for 256-bit (32 Bytes) keys.

	In few words, bigger keys will give you strongers encryptions. Remember that your keys must have exactly those lengths, it means that *'Example Key'* (length in bytes = 11) will raise you an exception.

:attr:`iv` **(Default: None)**
	The Initialization Vector (IV) will produce you a higher entropy in your encryption, especially when we work with block ciphers. A single invocation of the AES algorithm transforms a 128-bit plaintext block into a ciphertext block of 128 bits in size, it means that block ciphers need the same block size in our plain data. Obviously, most of the cases, this does not happen. For that reason we need to fill those empty spaces with something random, and that is the IV (16 Bytes). We always recommend to use an IV for any Block Cipher. For more information `Block Cipher Mode Operation <http://en.wikipedia.org/wiki/Block_cipher_mode_of_operation>`_.

