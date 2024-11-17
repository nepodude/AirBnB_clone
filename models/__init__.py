#!/usr/bin/python3
"""Creates a unique file storage instance
and calls it's reload method."""
from models.engine.file_storage import FileStorage


storage = FileStorage()

storage.reload()
