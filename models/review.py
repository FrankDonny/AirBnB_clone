#!/usr/bin/python3
"""module containing the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initialize from the parent class"""
        super().__init__(*args, **kwargs)
