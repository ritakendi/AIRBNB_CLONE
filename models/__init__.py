#!/usr/bin/python3
"""initializes the models pack"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
