#!/usr/bin/python3
"""
The file_storage module to be used in the Airbnb_clone project
"""
import json


class FileStorage:
    """FileStorage class for manipulating the file storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all the objects saved"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object on creation to the class __objects instance"""
        obj_ = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[obj_] = obj

    def save(self):
        """Saves new created instance into a storage file"""
        json_dict = {}
        for k, v in FileStorage.__objects.items():
            json_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(json_dict, file)

    def reload(self):
        """retrieves the information saved in the json file"""
        if FileStorage.__file_path is True:
            with open(FileStorage.__file_path, 'r',encoding="utf-8") as file:
                json_obj = json.load(file)
                for key, val in json_obj.items():
                    a_class = val["__class__"]
                    obj = eval(a_class + "(**val)")
                    FileStorage.__objects[key] = obj
        else:
            pass
