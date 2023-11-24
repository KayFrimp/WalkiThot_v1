#!venv/bin/python3
""" testing for the base model """
import unittest
import pycodestyle
import json
import os
from datetime import datetime
from models.base_model import BaseModel
basemodel = BaseModel()


class TestBaseModelDocs(unittest.TestCase):
    """ check for documentation """
    def test_class_doc(self):
        """check for class documentation"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation"""
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)


class TestBaseModelPycodestyle(unittest.TestCase):
    """ check for pycodestyle validation """
    def test_pycodestyle(self):
        """test base and test_base for pycodestyle conformance """
        style = pycodestyle.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestBaseModel(unittest.TestCase):
    """ tests for class BaseModels """
    @classmethod
    def setUpClass(cls):
        """setup instances for all tests """
        cls.basemodel = BaseModel()

    def test_id(self):
        """ test id """
        self.assertEqual(str, type(basemodel.id))

    def test_created_at(self):
        """test created_at """
        self.assertEqual(datetime, type(basemodel.created_at))

    def test_updated_at(self):
        """test updated_at """
        self.assertEqual(datetime, type(basemodel.updated_at))

    def test_to_dict(self):
        """ test to_dict method """
        new_dict = self.basemodel.to_dict()
        self.assertEqual(type(new_dict), dict)
        self.assertTrue('to_dict' in dir(basemodel))

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
