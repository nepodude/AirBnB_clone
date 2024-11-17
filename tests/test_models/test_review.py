#!/usr/bin/python3
"""Review module - contains the Review class that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class representing a review"""
    place_id = ""         # Place.id
    user_id = ""          # User.id
    text = ""
