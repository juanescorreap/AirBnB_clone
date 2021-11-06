#!/usr/bin/python3
"""
Class that defines FileStorage
"""
import json
import os



class FileStorage():
    """
    FileStorage definition
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return(self.__objects)

    def new(self, obj):
        if obj is not None:
            self.__objects.update(
                {str(type(obj).__name__ + "." + obj.id ): obj})


    def save(self):
        dict_serialized = {}
        if self.__objects is not None:
            for key, value in self.__objects.items():
                dict_serialized[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as my_file:
            json.dump(dict_serialized, my_file)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        dict_deserialized = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, encoding="utf-8") as my_file:
                content = my_file.read()
        else:
            return
        if content is not None or bool(content) is True:
            dict_deserialized = json.loads(content)
        for key, value in dict_deserialized.items():
            if key not in self.__objects.keys():
                ClassName = value["__class__"]
                new_instance = eval("{}(**value)".format(ClassName))
                self.new(new_instance)
        else:
            pass

