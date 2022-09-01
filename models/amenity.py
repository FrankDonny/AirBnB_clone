#!/usr/bin/python3
"""module containing the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialize from the parent class"""
        super().__init__(*args, **kwargs)
