import prompt
import random
from brain_games.scripts.brain_games import not_main


def main():
    player_name = not_main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    stage = 0

    while stage < 3:
        number = random.randint(0, 100)
        print(f"Question: {number}")
        yes_or_no = prompt.string("Your answer: ")
        if yes_or_no == "yes" and number % 2 == 0:
            print("Correct!")
            stage += 1
        elif yes_or_no == "no" and number % 2 != 0:
            print("Correct!")
            stage += 1
        else:
            if number % 2 == 0:
                correct_answer = "yes"
            elif number % 2 != 0:
                correct_answer = "no"
            return print(f"'{yes_or_no}' is wrong answer ;(.correct answer was '{correct_answer}'\nLet's try again, {player_name}!")
    return print(f'Congratulations, {player_name}!')


if __name__ == "__main__":
    main()
