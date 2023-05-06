from brain_games.cli import welcome_user


def start_and_find_name():
    print("Welcome to the Brain Games!")
    player_name = welcome_user()
    print(f"Hello, {player_name}!")
    return player_name
