#!/usr/bin/python3
import unittest
from models import base_model


class TestAirbnb(unittest.TestCase):

    def Test_BaseModel(self):
        new = base_model.BaseModel
        self.assertEqual(new, f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")


if __name__ == "__main__":
    unittest.main()
