#!/usr/bin/python3
"""module containing the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class inherits from BaseModel"""
    
    name = ""

    def __init__(self, *args, **kwargs):
        """initialize from the parent class"""
        super().__init__(*args, **kwargs)
