#!/usr/bin/python3
"""City module - contains the City class that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class representing a city"""
    state_id = ""  # State.id
    name = ""
