#!/usr/bin/python3
from brain_games.scripts.start import welcome
from brain_games.scripts.games.calc import operations
from brain_games.scripts.check import true_or_false
import prompt


def main():
    player_name = welcome()
    stage = 0
    print("What is the result of the expression?")
    while stage < 3:
        question, result, number1, number2, operate = operations()
        print(f"Question: {number1} {operate} {number2}")
        answer = prompt.string("Your answer: ")
        check = true_or_false(player_name, result, answer)
        if check is False:
            return
        stage += 1
    return print(f'Congratulations, {player_name}!')


if __name__ == "__main__":
    main()
