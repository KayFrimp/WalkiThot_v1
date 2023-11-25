#!venv/bin/python3
"""Response Class Module"""
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, mapped_column
from models.base_model import Base, BaseModel
import models


class Response(BaseModel, Base):
    """Response Class:

    Attributes:
        comment_id (string): Foreign Key (comment.id)
        reply (string): Response to a comment under a blog post
    """
    if models.storage_t == 'db':
        __tablename__ = 'responses'
        comment_id = mapped_column(String(60), ForeignKey('comments.id'))
        reply = mapped_column(String(255))
        comment = relationship("Comment", back_populates="responses")
    else:
        comment_id = ""
        reply = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
