#!/usr/bin/python3
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    player_name = welcome_user()
    print(f"Hello, {player_name}!")


if __name__ == "__main__":
    main()
