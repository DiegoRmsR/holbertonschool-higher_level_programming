#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        return length, None
    for char in sentence:
        if char == sentence[0]:
            break
    return length, char
