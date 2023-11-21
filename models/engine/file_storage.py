#!venv/bin/python3
""" filestorage module """
import json
from models.user import User
from models.comment import Comment
from models.blog import Categories, Blog
from models.response import Response
from models.base_model import BaseModel


class FileStorage:
    ''' FileStorage Class
    all: returns a json file of the storage
        Usage: self.all()
    new: sets in objects with key classname.id
        Usage: self.new(obj.id)
    save: convert __objects to JSON file
        Usage: self.save()
    reload: convert JSON file back to objects
        Usage: self.reload() '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
        Return:
        the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        sets in objects with key classname.id

        Args:
        object
        '''
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        '''
        serializes __objects to JSON file
        '''
        newdict = {}
        with open(self.__file_path, mode='w+', encoding='utf-8') as f:
            for k, v in self.__objects.items():
                newdict[k] = v.to_dict()
            json.dump(newdict, f)

    def reload(self):
        '''
        deserializies the JSON file
        '''
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                newobjects = json.load(f)
                for k, v in newobjects.items():
                    reloaded_obj = eval('{}(**v)'.format(v['__class__']))
                    self.__objects[k] = reloaded_obj

        except IOError:
            pass
