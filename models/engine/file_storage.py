#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from os import path
# from models.base_model import BaseModel  # Import BaseModel
# from models.user import User  # Import User class
# from models.place import Place  # Import the Place class
# from models.state import State  # Import the State class
# from models.city import City  # Import the City class
# from models.amenity import Amenity  # Import the Amenity class
# from models.review import Review  # Import the Review class


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    # __instance = None

    # def __new__(cls):
    # if cls.__instance is None:
    # cls.__instance = super().__new__(cls)
    # return cls.__instance

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        or Returns the list of objects of one type of class.
        """
        if cls is None:
            return self.__objects
        return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        # return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        # key = obj.__class__.__name__ + '.' + obj.id
        # key = "{}.{}".format(type(obj).__name__, obj.id)
        # print("key in new:", key)  # Debugging output
        # FileStorage.__objects[key] = obj
        # key = "{}.{}".format(type(obj).__name__, obj.id)
        # self.__objects[key] = obj
        # print("Added object:", obj)  # Debugging output
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                # for key, val in FileStorage.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)
            # json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
                # class_name = val['__class__']
                # del val['__class__']
                # obj = classes[class_name](**val)
                # self.__objects[key] = obj
                # obj = eval(class_name)(**val)
                # key = class_name + '.' + obj.id
                # FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside."""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects.pop(key, None)
