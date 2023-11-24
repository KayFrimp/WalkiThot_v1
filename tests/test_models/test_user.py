import unittest
import pycodestyle
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.blog import Blog
from models.comment import Comment
from models.response import Response
from models.engine.file_storage import FileStorage
user = User()


class TestUserDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(User.__doc__) > 0)


class TestUserPycodestyle(unittest.TestCase):
    """ check for the pycodestyle compliance """
    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(quiet=True)
        file1 = 'models/user.py'
        file2 = 'tests/test_models/test_user.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestUser(unittest.TestCase):
    """ testing several terms on the user file"""
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    def test_subclass(self):
        """ test that user is a subclass of basemodel """
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_id(self):
        """ test the id of user"""
        self.assertEqual(str, type(user.id))

    def test_email(self):
        """ test the email of user"""
        self.assertEqual(str, type(user.email))

    def test_password(self):
        """ test the password """
        self.assertEqual(str, type(user.password))

    def test_first_name(self):
        """ test the first name"""
        self.assertEqual(str, type(user.first_name))

    def test_last_name(self):
        """ test the last name """
        self.assertEqual(str, type(user.last_name))

    def test_cohort(self):
        """ test the cohort of the user """
        self.assertEqual(type(None), type(user.cohort))

    @classmethod
    def tearDownClass(cls):
        """ remove test instances """
        pass
