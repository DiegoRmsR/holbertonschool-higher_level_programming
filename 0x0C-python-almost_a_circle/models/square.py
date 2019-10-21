#!/usr/bin/python3
""" class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    " Class Square "
    def __init__(self, size, x=0, y=0, id=None):
        " Init Instances "
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        argm = "({}) {}/{} - ".format(self.id, self.x, self.y)
        argm += "{}".format(self.size)
        return "[Square] " + argm

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """"Method that assigns attributes:"""
        l_attr = ['id', 'size', 'x', 'y']
        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, l_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                for i in range(len(l_attr)):
                    if l_attr[i] == key:
                        setattr(self, key, value)

    def to_dictionary(self):
        new_d = {
                "id": self.id, "size": self.size,
                "x": self.x, "y": self.y
                }
        return new_d
