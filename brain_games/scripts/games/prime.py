from random import randint

def yes_or_no():
    question = randint(3, 50)
    for num in range(2, question):
        if question % num == 0:
            result = "no"
            return question, result
    result = "yes"
    return question, result

