#!/usr/bin/python3
""" class Square that inherits from Rectangle """ 
from models.rectangle import Rectangle


class Square(Rectangle):
    " Class Square "
    def __init__(self, size, x=0, y=0, id=None):
        " Init Instances "

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        argm = "({}) {}/{} - ".format(self.id, self.x, self.y)
        argm += "{}".format(self.width)
        return "[Square] " + argm
