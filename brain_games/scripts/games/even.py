from random import randint


def parity():
    question = randint(0, 100)
    if question % 2 == 0:
        result = "yes"
    elif question % 2 != 0:
        result = "no"
    return question, result
