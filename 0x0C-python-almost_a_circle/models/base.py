#!/usr/bin/python3
""" Class Base"""
import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init instances """
        self.__nb_objects = 0

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Method that returns the JSON string
        representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Method that writes the JSON string
        representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        new_l = []
        list = ""
        with open(filename, "w") as f:
            if list_objs is None:
                f.write(new_l)
            else:
                for i in list_objs:
                    new_l.append(i.to_dictionary())
                list = cls.to_json_string(new_l)
            f.write(list)
