from math import gcd
from random import randint

def operations():
        multiplier = randint(1, 10) ###часто выпдала единица НОД и решил добавить разнообразия таким образом
        number_one = randint(1, 10) * multiplier
        number_two = randint(1, 10) * multiplier
        result = str(gcd(number_one, number_two))
        question = str(number_one) + " " + str(number_two)
        return question, result
