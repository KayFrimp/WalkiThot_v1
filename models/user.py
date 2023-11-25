#!venv/bin/python3
""" This is a user class definition """
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, relationship
import models
from models.base_model import Base, BaseModel
from models.blog import Blog


class User(BaseModel, Base):
    """ user class definition with the needed attribute """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = mapped_column(String(128), nullable=False)
        password = mapped_column(String(128), nullable=False)
        first_name = mapped_column(String(128), nullable=False)
        last_name = mapped_column(String(128), nullable=True)
        cohort = mapped_column(Integer, nullable=True)
        blogs = relationship("Blog", back_populates="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        cohort = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        def blogs(self):
            """getter for list of Blog instances related to the user"""
            blog_list = []
            all_blogs = models.storage.all(Blog)
            for blog in all_blogs.values():
                if blog.user_id == self.id:
                    blog_list.append(blog)
            return blog_list
