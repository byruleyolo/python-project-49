from random import randint, choice


def operations():
    number_one = randint(0, 20)
    number_two = randint(0, 20)
    what_operate = choice(["+", "-", "*"])
    match what_operate:
        case "+":
            question = str(number_one) + "+" + str(number_two)
            result = str(number_one + number_two)
        case "-":
            question = str(number_one) + "-" + str(number_two)
            result = str(number_one - number_two)
        case "*":
            question = str(number_one) + "*" + str(number_two)
            result = str(number_one * number_two)
    number_one = str(number_one)
    number_two = str(number_two)
    return question, result, number_one, number_two, what_operate
