from brain_games.scripts.start import welcome
from brain_games.scripts.games.prime import yes_or_no
from brain_games.scripts.check import true_or_false
import prompt


def main():
    player_name = welcome()
    stage = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while stage < 3:
        question, result = yes_or_no()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        check = true_or_false(player_name, result, answer)
        if check is False:
            return
        stage += 1
    return print(f'Congratulations, {player_name}!')


if __name__ == "__main__":
    main()
