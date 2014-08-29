class EncryptionKeyException(Exception):
	def __init__(self, value=None):
		if value:
			self.value = value
		else:
			self.value = 'You didn\'t introduce a valid encryption key. Did you forget the key '\
			'param in the field? or you forgot that AES keys have to be 16, 24 or 32 bytes long?'
	def __str__(self):
		return repr(self.value)
