#!venv/bin/python3
"""DBStorage Class Module"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os

from models.base_model import Base
from models.user import User
from models.blog import Blog
from models.comment import Comment
from models.response import Response

# Environment variables
mysql_user = os.getenv('WALKI_MYSQL_USER')
mysql_password = os.getenv('WALKI_MYSQL_PWD')
mysql_host = os.getenv('WALKI_MYSQL_HOST')
mysql_db = os.getenv('WALKI_MYSQL_DB')
walki_env = os.getenv('WALKI_ENV')

classes = {"User": User, "Blog": Blog,
           "Comment": Comment, "Response": Response}


class DBStorage:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                mysql_user,
                mysql_password,
                mysql_host,
                mysql_db
            ), pool_pre_ping=True)

        if walki_env == 'test':
            metadata = MetaData()
            # Reflect all existing tables from database into the MetaData obj
            metadata.reflect(self.__engine)
            # Drop all the tables
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """Returns the object based on the class and id or None if not found"""
        if cls in classes.values():
            objs = self.all(cls)
            for value in objs.values():
                if value.id == id:
                    return value
        return None

    def count(self, cls=None):
        """Returns number of objects in storage matching given class"""
        objs = {}
        if cls is None or cls in classes.values():
            objs = self.all(cls)
        return len(objs)
