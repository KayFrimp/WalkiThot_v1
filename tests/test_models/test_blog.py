#!venv/bin/python3
import unittest
import pycodestyle
import os
from datetime import datetime
from models.base_model import BaseModel
from models.blog import Blog
from models.user import User
from models.comment import Comment
from models.response import Response
from models.engine.file_storage import FileStorage
blog = Blog()


class TestBlogDocs(unittest.TestCase):
    """ check for documentation"""
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Blog.__doc__) > 0)


class TestUserPycodestyle(unittest.TestCase):
    """ check for the pycodestyle compliance """
    def test_pycodestyle(self):
        """ check for pycodestyle """
        style = pycodestyle.StyleGuide(quiet=True)
        file1 = 'models/blog.py'
        file2 = 'tests/test_models/test_blog.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).s")


class TestBlog(unittest.TestCase):
    """ testing several terms on the blog files """
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    def test_subclass(self):
        """ test that blog is a subclass of basemodel"""
        self.assertIsInstance(blog, BaseModel)
        self.assertTrue(hasattr(blog, 'id'))
        self.assertTrue(hasattr(blog, 'created_at'))
        self.assertTrue(hasattr(blog, 'updated_at'))

    def test_title(self):
        """ test the type of each variables on blog"""
        self.assertEqual(str, type(blog.title))

    def test_content(self):
        """ test the content in blog """
        self.assertEqual(str, type(blog.content))

    def test_type(self):
        """ test the type in blog"""
        self.assertEqual(type(None), type(blog.type))

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
