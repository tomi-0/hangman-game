# Hangman game

import random

words = ("maths", "english", "history", "art", "geography", "spanish")

# dictionary of hangman art from @chrishorton
hangman_art = {
    0: (
    """
    +---+
    |   |
        |
        |
        |
        |
    ========="""
    ),
    1: (
    """
    +---+
    |   |
    O   |
        |
        |
        |
    ========="""
    ),
    2: (
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    ========="""
    ),
    3: (
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    ========="""
    ),
    # r - raw string w/ no escape sequences
    4: (
    r"""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    ========="""
    ),
    5: (
    r"""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    ========="""
    ),
    6: (
    r"""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    ========="""
    ),
}

def display_man(wrong_guesses):
    print(hangman_art.get(wrong_guesses))


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print("The correct answer was: "+" ".join(answer))


def main():
    answer = random.choice(words)
    hint = list("_" * len(answer))
    wrong_guesses = 0
    guesseed_letters = []
    game_over = False
    
    print()
    print("-------------------------------")
    print("|  Welcome to Python Hangman! |")
    print("-------------------------------")

    while not game_over:
        
        display_man(wrong_guesses)
        display_hint(hint)

        print()
        print(f"{6-wrong_guesses} incorrect guesses left")
        guess = input("Enter a letter guess: ").lower()
        print()

        if guess in guesseed_letters:
            print("You've already guessed this letter")
        else:
            guesseed_letters.append(guess)
        
            if guess in answer:
                for i in range(0,len(answer)):
                    if answer[i] == guess:
                        hint[i] = guess
            else:
                wrong_guesses += 1
                if wrong_guesses == 6:
                    display_man(wrong_guesses)
                    print()
                    display_answer(answer)
                    break

        if "_" not in hint:
            print("-------------------------------")
            print("Well done you got it!")
            display_answer(answer)
            game_over = True

    print("Game over!")
    print("-------------------------------")


if __name__ == "__main__":
    main()


