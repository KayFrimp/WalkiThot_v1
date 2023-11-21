#!venv/bin/python3
"""Base Model Class For WalkiThot"""
from datetime import datetime
import uuid


class BaseModel:
    """BaseModel Class:

    Attributes:
        id (string): Unique identifier
        created_at (datetime): date created
        update_at (datetime): date updated
    """

    def __init__(self, **kwargs):
        """Initializes the BaseModel class
    
        Args:
            **kwargs (dictionary): contains all arguments by key/value
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {str(self.__dict__)}"

    def save(self):
        """Updates public instance attribute update_at with current datetime"""
        self.updated_at = datetime.now()

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
        return instance_dict
