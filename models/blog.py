#!venv/bin/python3
"""Blog Class Module"""
from models.base_model import BaseModel


class Blog(BaseModel):
    """Blog Class Definition

    Attributes:
        title (string): Blog post Title
        type (pending): Category blog post falls under
        content (string): Blog post
    """
    title = ""
    type = ""
    content = ""
