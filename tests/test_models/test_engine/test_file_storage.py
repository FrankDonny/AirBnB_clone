#!/usr/bin/python3
"""unittest module for the storage_file engine"""
import models.engine.file_storage
import models.base_model
import unittest


class TestFileStorage(unittest.TestCase):
    """test class for the File_Storage"""
    store = models.engine.file_storage.FileStorage()

    def test_all(self):
        """testing the 'all' method of the file_storage"""
        new = models.base_model.BaseModel()
        new1 = models.base_model.BaseModel()
        self.store.save()
        objs = self.store.all()
        num = len(objs)
        self.assertEqual(num, 2)

    def test_new(self):
        """testing the 'new' method of the file_storage"""
        new = models.base_model.BaseModel()
        new.name = "Nelly"
        self.store.save()
        objs = self.store.all()
        ky = str(new.__class__.__name__) + "." + str(new.id)
        self.assertIn(ky, objs)

    def test_save(self):
        """testing the 'save' method of the file_storage"""
        new = models.base_model.BaseModel()
        new.name = "Nelly"
        self.store.save()
        self.assertEqual(getattr(new, "name"), "Nelly")


if __name__ == '__main__':
    unittest.main()
