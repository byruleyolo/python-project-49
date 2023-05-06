import prompt
from random import randint, choice
from brain_games.scripts.run import start_and_find_name


def main():
    player_name = start_and_find_name()
    stage = 0
    print("What is the result of the expression?")
    while stage < 3:
        number_one = randint(0, 20)
        number_two = randint(0, 20)
        what_operate = ["+", "-", "*"]
        match choice(what_operate):
            case "+":
                print("Question: " + str(number_one) + "+" + str(number_two))
                result = number_one + number_two
            case "-":
                print("Question: " + str(number_one) + "-" + str(number_two))
                result = number_one - number_two
            case "*":
                print("Question: " + str(number_one) + "*" + str(number_two))
                result = number_one * number_two
        answer = prompt.string("Your answer: ")
        if str(result) == answer:
            print("Correct!")
            stage += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'")
            return print(f"Let's try again, {player_name}!")
    return print(f'Congratulations, {player_name}!')


if __name__ == "__main__":
    main()
