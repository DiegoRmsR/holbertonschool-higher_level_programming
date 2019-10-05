#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
TypeError: text must be a string
Return: nothing
"""
def text_indentation(text):
    """
    prints a text with 2 new lines
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace(". ", ".\n\n")
    text = text.replace(": ", ":\n\n")
    text = text.replace("? ", "?\n\n")

    print(text)
