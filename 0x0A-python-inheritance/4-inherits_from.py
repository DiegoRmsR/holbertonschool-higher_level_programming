#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    function that verifies if is an instance of a class
    that inherited (directly or indirectly)

    Return True if is an instance of a class
    Return False otherwise
    """

    if isinstance(obj, a_class) and type(obj) is a_class:
        return(False)
    else:
        return(True)
