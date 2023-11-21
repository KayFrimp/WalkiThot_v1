#!venv/bin/python3
"""Response Class Module"""
from models.base_model import BaseModel


class Response(BaseModel):
    """Response Class:

    Attributes:
        comment_id (string): Foreign Key (comment.id)
        reply (string): Response to a comment under a blog post
    """

    comment_id = ""
    reply = ""
