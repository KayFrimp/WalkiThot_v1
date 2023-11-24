import unittest
import pycodestyle
import os
from models.base_model import BaseModel
from models.comment import Comment
from models.blog import Blog
from models.response import Response
from models.user import User
from models.engine.file_storage import FileStorage
comment = Comment()


class TestCommentDocs(unittest.TestCase):
    """ test the documentation of the class """
    def test_comment_doc(self):
        """test the documentations """
        self.assertTrue(len(Comment.__doc__) > 0)


class TestCommentPycodestyle(unittest.TestCase):
    """ test the pycodestyle compliance """
    def test_comment_pycodestyle(self):
        style = pycodestyle.StyleGuide()
        file1 = 'models/comment.py'
        file2 = 'tests/test_models/test_comment.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestComment(unittest.TestCase):
    """ testing each case of and variables of comment """
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    def test_blog_id(self):
        self.assertEqual(str, type(comment.blog_id))

    def test_comment(self):
        self.assertEqual(str, type(comment.comment))

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
