#!/usr/bin/python3
"""
Class Base
"""
import json
import os.path as path


class Base:
    """
    Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init instances
        """
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
        if list_objs:
            for i in list_objs:
                new_l.append(i.to_dictionary())
        list = cls.to_json_string(new_l)

        with open(filename, "w") as f:
            f.write(list)

    @staticmethod
    def from_json_string(json_string):
        """ Method that returns the list of the
        JSON string representation json_string """

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Method that that returns an instance
        with all attributes already set """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Method that returns a list of instances
        """
        filename = cls.__name__ + ".json"
        dir_r = ""
        new_l = []
        list = []
        if path.exists(filename) is False:
            return new_l
        else:
            with open(filename, 'r') as f:
                dir_r = f.read()
                new_l = cls.from_json_string(dir_r)
                for i in new_l:
                    list.append(cls.create(**i))
            return list
