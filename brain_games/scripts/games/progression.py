from random import randint


def operations():
    index = 0
    progression_number = randint(1, 10)
    question = ""
    list = []
    first_number = randint(0, 100)
    while index != 10:
        index += 1
        first_number += progression_number
        list.append(str(first_number))
    missing = randint(0, 9)
    result = list[missing]
    list[missing] = ".. "
    for i in list:
        question = question + i + " "
    return question, result
