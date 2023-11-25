#!venv/bin/python3
"""Base Model Class For WalkiThot"""
from sqlalchemy import DateTime, String
from sqlalchemy.orm import DeclarativeBase, mapped_column
from datetime import datetime
import uuid

import models

if models.storage_t == 'db':
    class Base(DeclarativeBase):
        pass
else:
    Base = object


class BaseModel:
    """BaseModel Class:

    Attributes:
        id (string): Unique identifier
        created_at (datetime): date created
        update_at (datetime): date updated
    """
    if models.storage_t == 'db':
        id = mapped_column(String(60), primary_key=True)
        created_at = mapped_column(DateTime, default=datetime.utcnow)
        updated_at = mapped_column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel class

        Args:
            **kwargs (dictionary): contains all arguments by key/value
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            if kwargs.get('created_at', None) and type(self.created_at) is str:
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
            else:
                self.created_at = datetime.now()
            if kwargs.get('updated_at', None) and type(self.updated_at) is str:
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
            else:
                self.updated_at = self.created_at
            if kwargs.get('id', None) is None:
                self.id = str(uuid.uuid4())
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {str(self.__dict__)}"

    def save(self):
        """Updates public instance attribute update_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary of all keys/values of
        __dict__ of the instance"""
        instance_dict = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                instance_dict[key] = value.isoformat()
            else:
                instance_dict[key] = value
        instance_dict['__class__'] = self.__class__.__name__
        if '_sa_instance_state' in instance_dict:
            del instance_dict["_sa_instance_state"]
        return instance_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
