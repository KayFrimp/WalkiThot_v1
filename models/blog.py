#!venv/bin/python3
"""Blog Class Module"""
from models.base_model import BaseModel
from enum import Enum


class Category(Enum):
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


class Blog(BaseModel):
    """Blog Class Definition

    Attributes:
        title (string): Blog post Title
        type (Category): Category blog post falls under
        content (string): Blog post
    """
    title = ""
    type = None
    content = ""
