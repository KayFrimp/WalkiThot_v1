#!venv/bin/python3
"""Blog Class Module"""
from sqlalchemy import Enum, ForeignKey, LargeBinary, String, Text
from sqlalchemy.orm import mapped_column, relationship
import models
from models.base_model import BaseModel, Base
from enum import Enum as PyEnum

from models.comment import Comment


class Category(str, PyEnum):
    """
    Enumeration representing categories for blog posts.

    Each value in the enum corresponds to a category.
    """
    DEVELOPMENT = "Web & Mobile Development"
    CLOUD = "Cloud Computing"
    AI = "Artificial Intelligence & Machine Learning"
    DATA = "Data Science & Analytics"
    CYBERSECURITY = "Cybersecurity"
    IOT = "Internet of Things(Iot)"
    NEWS = "Tech News & Trends"
    ENTREPRENEURSHIP = "Entrepreneurship"
    OTHER = "Other..."


class Blog(BaseModel, Base):
    """Blog Class Definition

    Attributes:
        title (string): Blog post Title
        type (Category): Category blog post falls under
        content (string): Blog post
    """
    if models.storage_t == 'db':
        __tablename__ = 'blogs'
        user_id = mapped_column(String(60),
                                ForeignKey('users.id'), nullable=False)
        title = mapped_column(String(255), nullable=False)
        type = mapped_column(Enum(Category), default=Category.OTHER,
                             nullable=False)
        content = mapped_column(Text, nullable=False)
        image = mapped_column(LargeBinary, nullable=True)
        user = relationship("User", back_populates="blogs")
        comments = relationship("Comment", back_populates="blog",
                                cascade='all, delete-orphan')
    else:
        user_id = ""
        title = ""
        type: Category = None
        content = ""
        image = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def comments(self):
            """getter for list of Comment instances related to the blog"""
            comment_list = []
            all_comments = models.storage.all(Comment)
            for comment in all_comments.values():
                if comment.blog_id == self.id:
                    comment_list.append(comment)
            return comment_list
