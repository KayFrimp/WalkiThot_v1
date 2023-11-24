#!venv/bin/python3
import unittest
import pycodestyle
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.comment import Comment
from models.blog import Blog
from models.response import Response
from models.engine.file_storage import FileStorage

""" test for file storage engine"""


class TestFileStorageDocs(unittest.TestCase):
    """ check for the documentation """
    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(FileStorage.__doc__) > 0)


class TestFileStoragePycodestyle(unittest.TestCase):
    """ check for pycodestyle validation """
    def test_pycodestyle(self):
        """ test base and test_base for pycodestyle conformance """
        style = pycodestyle.StyleGuide(quiet=True)
        file1 = 'models/engine/file_storage.py'
        file2 = 'tests/test_models/test_engine/test_file_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning). ")


class TestFileStorage(unittest.TestCase):
    """ tests for class FileStorage """
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    def test_all(self):
        """ test all method """
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
