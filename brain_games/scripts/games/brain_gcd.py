from brain_games.scripts.run import start_and_find_name
from math import gcd
from random import randint
import prompt

def main():
    player_name = start_and_find_name()
    stage = 0
    print("Find the greatest common divisor of given numbers.")
    while stage < 3:
        multiplier = randint(1, 10) ###часто выпдала единица НОД и решил добавить разнообразия таким образом
        number_one = randint(1, 10) * multiplier
        number_two = randint(1, 10) * multiplier
        result = gcd(number_one, number_two)
        stage +=1
        print('Question: ' + str(number_one) + " " + str(number_two))
        answer = prompt.string("Your answer: ")
        if str(result) == answer:
            print("Correct!")
        else:
           return print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'\nLet's try again, {player_name}!")
    return print(f'Congratulations, {player_name}!')


if __name__ == "__main__":
    main()
