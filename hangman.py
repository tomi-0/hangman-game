# Hangman game

import random

words = ("maths", "english", "history", "art", "geography", "spanish" )

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

print(hangman_art.get(0))

