#!/usr/bin/python3
from models.base_model import BaseModel
import unittest


class TestAirbnb(unittest.TestCase):
    def Test_BaseModel(self):
        new = BaseModel()
        self.assertEqual(new, f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")


if __name__ == "__main__":
    unittest.main()
