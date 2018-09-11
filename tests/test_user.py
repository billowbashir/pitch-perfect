import unittest
from app.models import User
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(username='bashir',email='new@gmail.com',password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password,('banana'))
    def test_instance(self):
         self.assertEquals(self.new_user.username,'bashir')
         self.assertEquals(self.new_user.email,'new@gmail.com')
