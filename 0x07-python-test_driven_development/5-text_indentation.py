#!/usr/bin/python3
"""Indent text module"""


def text_indentation(text):
    """Function that prints a text with
    2 new lines after each of these characters: ., ?

    Args:
        text (str): text to indent

    Raises:
        TypeError: if no str type
    """
    newText = ""
    sentence = ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    pos = 0
    while pos in range(len(text)):
        letter = text[pos]
        if letter not in (".", "?", ":"):
            sentence += letter
        else:
            sentence += letter
            try:
                while sentence[0] == " ":
                    sentence = sentence[1:]
            except IndexError:
                pass
            try:
                while sentence[len(sentence)-1] == " ":
                    sentence = sentence[:-1]
            except IndexError:
                pass
            newText = newText + sentence + "\n\n"
            sentence = ""
        pos = pos+1
    try:
        while sentence[0] == " ":
            sentence = sentence[1:]
    except IndexError:
        pass
    try:
        while sentence[len(sentence)-1] == " ":
            sentence = sentence[:-1]
    except IndexError:
        pass
    newText = newText + sentence
    print(newText, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
