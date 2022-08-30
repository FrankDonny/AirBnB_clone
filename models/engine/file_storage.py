#!/usr/bin/python3
"""
The file_storage module to be used in the Airbnb_clone project
"""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        obj_ = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[obj_] = obj

    def save(self):
        json_dict = {}
        for k, v in FileStorage.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(json_dict, file)

    def reload(self):
        if FileStorage.__file_path is True:
            with open(FileStorage.__file_path, encoding="utf-8") as file:
                json_obj = json.loads(file.read())
                return json_obj
        else:
            pass
