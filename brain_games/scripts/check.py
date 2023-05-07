def true_or_false(player_name, result, answer):
    if result == answer:
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'")
        print(f"Let's try again, {player_name}!")
        return False
