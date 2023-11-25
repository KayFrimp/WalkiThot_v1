#!venv/bin/python3
"""Comment class Module"""
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base_model import Base, BaseModel
import models
from models.response import Response


class Comment(BaseModel, Base):
    """Comment class definition:

    Attributes:
        blog_id (string): Foreign key (blog.id)
        comment (string): Any comment under a blog post
    """
    if models.storage_t == 'db':
        __tablename__ = 'comments'
        blog_id = mapped_column(String(60),
                                ForeignKey('blogs.id'), nullable=False)
        comment = mapped_column(String(255), nullable=False)
        responses = relationship("Response", back_populates="comment")
        blog = relationship("Blog", back_populates="comments")
    else:
        blog_id = ""
        comment = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        def reponses(self):
            """getter for list of Response instances related to the comment"""
            response_list = []
            all_responses = models.storage.all(Response)
            for response in all_responses.values():
                if response.comment_id == self.id:
                    response_list.append(Response)
            return response_list
