import random


class Hangman:
    def __init__(self, title: str = "H A N G M A N",
                 announcement: str = "The game will be available soon.",
                 guessed_words=None):
        if guessed_words is None:
            guessed_words = ["python", "java", "kotlin", "javascript"]
        self.title = title
        self.announcement = announcement
        self.guessed_words = guessed_words

    def print_title(self):
        print(self.title)

    def print_announce(self):
        print(self.announcement)

    def check_word(self, user_word: str):
        guessed_word = random.choice(self.guessed_words)  # Random choice guessed word
        return user_word == guessed_word


hangman = Hangman()

hangman.print_title()
word: str = input("Guess the word: > ")
if hangman.check_word(word):
    print("You survived!")
else:
    print("You are hanged!")
