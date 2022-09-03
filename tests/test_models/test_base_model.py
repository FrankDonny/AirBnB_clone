#!/usr/bin/python3
"""unit testing the base model module"""
import models.base_model
from models import storage
import unittest


class TestBaseModel(unittest.TestCase):
    """The TestBaseModel class for testing the base_model"""

    def setUp(self):
        """creating a new object for the class"""
        self.new = models.base_model.BaseModel()

    def test_init(self):
        """testing the init function"""
        self.assertIsInstance(self.new, models.base_model.BaseModel)
        self.assertTrue(self.new.id)
        self.assertTrue(self.new.created_at)
        self.assertTrue(self.new.updated_at)

    def test_storage(self):
        """checking the storage"""
        obj = storage.all()
        key = str(self.new.__class__.__name__) + "." + str(self.new.id)
        self.assertIn(key, obj)

    def test_dict(self):
        """test for checking about the to_dict method"""
        _dict = self.new.to_dict()
        self.assertTrue(_dict)
        self.new.name = "My base Model"
        self.assertIn("name", self.new.__dict__)

    def test_save(self):
        """test for checking if the instance got saved"""
        self.new.name = "My base Model"
        self.assertFalse(self.new.save())


if __name__ == '__main__':
    unittest.main()
