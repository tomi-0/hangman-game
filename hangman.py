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
    for char in hint:
        print(char, end=" ")
    print() 
    print()

def display_answer():
    pass

def main():
    answer = random.choice(words)
    hint = "_" * len(answer)
    wrong_guesses = 0
    game_over = False
    
    print("Welcome to Python Hangman")

    while not game_over:
        
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter guess: ").lower()
        if guess in answer:
            for char in answer:
                if char == guess:
                    print()
        else:
            wrong_guesses += 1
            if wrong_guesses == 6:
                display_answer()
                break

    print("Game over!")

if __name__ == "__main__":
    main()


