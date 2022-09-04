#!/usr/bin/python3
"""module containing the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initialize from the parent class"""
        super().__init__(*args, **kwargs)
