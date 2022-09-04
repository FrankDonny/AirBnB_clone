#!/usr/bin/python3
"""This is a test module containing the console test"""
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from os import remove
import unittest


class TestConsole(unittest.TestCase):
    """The console test class"""

    def tearDown(self):
        """Tear down method to delete file after the test is done executing"""
        remove("file.json")

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
