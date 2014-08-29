from mongoengine import *
from base.fields import EncryptedField

__all__ = [
    'EncryptedEmailField', 'EncryptedStringField', 'EncryptedIntField', 'EncryptedDecimalField', 'EncryptedFloatField','EncryptedLongField']

class EncryptedEmailField(EncryptedField,EmailField):
    internal_type = type(EmailField())

    def __get__(self, instance, owner):
        value=super(EncryptedEmailField, self).__get__(instance, owner)
        return self.to_python(value)

    def validate(self, value):
        super(EncryptedEmailField, self).validate(self.decrypt_value(value))

class EncryptedStringField(EncryptedField,StringField):
    internal_type = type(StringField())

    def __get__(self, instance, owner):
        value=super(EncryptedStringField, self).__get__(instance, owner)
        return self.to_python(value)

    def validate(self, value):
        super(EncryptedStringField, self).validate(self.decrypt_value(value))

class EncryptedIntField(EncryptedField,IntField):
    internal_type = type(IntField())

    def __get__(self, instance, owner):
        value=super(EncryptedIntField, self).__get__(instance, owner)
        return self.to_python(value)

    def validate(self, value):
        super(EncryptedIntField, self).validate(self.decrypt_value(value))

class EncryptedDecimalField(EncryptedField,DecimalField):
    internal_type = type(DecimalField())

    def __get__(self, instance, owner):
        value=super(EncryptedDecimalField, self).__get__(instance, owner)
        return self.to_python(value)

    def validate(self, value):
        super(EncryptedDecimalField, self).validate(self.decrypt_value(value))

class EncryptedFloatField(EncryptedField,FloatField):
    internal_type = type(FloatField())

    def __get__(self, instance, owner):
        value=super(EncryptedFloatField, self).__get__(instance, owner)
        return self.to_python(value)

    def validate(self, value):
        super(EncryptedFloatField, self).validate(float(self.decrypt_value(value)))

class EncryptedLongField(EncryptedField,LongField):
    internal_type = type(FloatField())

    def __get__(self, instance, owner):
        value=super(EncryptedLongField, self).__get__(instance, owner)
        return self.to_python(value)

    def validate(self, value):
        super(EncryptedLongField, self).validate(self.decrypt_value(value))
