#!/usr/bin/python3
"""Amenity module - contains the Amenity class that inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class representing an amenity"""
    name = ""
