import random 
class Hangman:
    class Hangman:
        possible_words: List[str] = ["becode", "learning", "mathematics", "sessions"]

    def __init__(self):
        self.word_to_find: List[str] = []
        self.lives: int = 5
        self.well_guessed_letters: List[str] = []
        self.bad_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

        for letter in random.choice(Hangman.possible_words):
            self.word_to_find.append(letter) 
            self.well_guessed_letters.append('_')
    