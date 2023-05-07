from brain_games.scripts.start import welcome
from brain_games.scripts.games.progression import operations
from brain_games.scripts.check import true_or_false
import prompt


def main():
    player_name = welcome()
    stage = 0
    print("What number is missing in the progression?")
    while stage < 3:
        question, result = operations()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        check = true_or_false(player_name, result, answer)
        if check is False:
            return
        stage += 1
    return print(f'Congratulations, {player_name}!')


if __name__ == "__main__":
    main()
