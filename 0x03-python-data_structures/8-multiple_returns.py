def multiple_returns(sentence):
    length = len(sentence)
    for char in sentence:
        if char == sentence[0]:
            break
    return length, char
