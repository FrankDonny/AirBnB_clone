#!/usr/bin/python3
"""module containing the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inherits from BaseModel"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialize from the parent class"""
        super().__init__(*args, **kwargs)
