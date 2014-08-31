#!/usr/bin/python
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from securemongoengine.fields import *
import unittest,decimal
from models import *

class TestEncryption32(unittest.TestCase):
    def setUp(self):
        self.user1 = User(name='Juan',lastname='Urrego',email='js.urrego@novcat.co',password = '123456', phone_number=11234567,money=243.23,age=26,height=1.75)
        self.user2 = User(name='Juan',lastname='Otro',email='js.urrego@novcat.com.co',password = '123456', phone_number=76543211)
        connect('test', host='127.0.0.1')
        User.objects().delete()

    def test_save_encrypted(self):
        self.user1.save()
        self.assertEqual(User.objects().first().name, 'Juan')
        self.assertEqual(User.objects().first().lastname, 'Urrego')
        self.assertEqual(User.objects().first().email, 'js.urrego@novcat.co')
        self.assertEqual(User.objects().first().password, '123456')
        self.assertEqual(User.objects().first().phone_number, 11234567)
        self.assertEqual(User.objects().first().money, decimal.Decimal('243.23'))
        self.assertEqual(User.objects().first().age, 26)
        self.assertEqual(User.objects().first().height, 1.75)

        print User.objects().first().to_mongo()
        

class TestEncryption24(unittest.TestCase):
    pass


class TestEncryption16(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()


