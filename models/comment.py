#!venv/bin/python3
"""Comment class Module"""
from models.base_model import BaseModel


class Comment(BaseModel):
    """Comment class definition:

    Attributes:
        blog_id (string): Foreign key (blog.id)
        comment (string): Any comment under a blog post
    """

    blog_id = ""
    comment = ""
