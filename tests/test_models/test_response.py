import unittest
import pycodestyle
import os
from datetime import datetime
from models.base_model import BaseModel
from models.response import Response
from models.user import User
from models.blog import Blog
from models.comment import Comment
from models.engine.file_storage import FileStorage
response = Response()


class TestUserDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Comment.__doc__) > 0)


class TestResponsePycodestyle(unittest.TestCase):
    """test pycodestyle compliance"""
    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(quiet=True)
        file1 = 'models/response.py'
        file2 = 'tests/test_models/test_response.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestResponse(unittest.TestCase):
    """ testing several terms and variables in response"""
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    def test_subclass(self):
        """ test that response is a subclass of basemodel"""
        self.assertIsInstance(response, BaseModel)
        self.assertTrue(hasattr(response, "id"))
        self.assertTrue(hasattr(response, 'created_at'))
        self.assertTrue(hasattr(response, 'updated_at'))

    def test_comment_id(self):
        self.assertEqual(str, type(response.comment_id))

    def test_reply(self):
        self.assertEqual(str, type(response.reply))

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
