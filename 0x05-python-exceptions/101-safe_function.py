#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        execute = fct(*args)
    except Exception as Error:
        print("Exception:", Error, file=sys.stderr)
        return None
    return execute
