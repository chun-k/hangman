import random
from hangpkg.hang_class import *

if __name__ == '__main__':
    word_to_guess = random.choice(WORDS)
    hangman = Hangman(word_to_guess)
    hangman.play()
