import random


class Hangman:
    def __init__(self, title: str = "H A N G M A N",
                 announcement: str = "The game will be available soon.",
                 guess_words=None):
        if guess_words is None:
            guess_words = ["python", "java", "kotlin", "javascript"]
        self.title = title
        self.announcement = announcement
        self.guess_words = guess_words

    def print_title(self):
        print(self.title)

    def print_announce(self):
        print(self.announcement)

    def check_word(self, user_word: str):
        guess_word = random.choice(self.guess_words)
        return user_word == guess_word


hangman = Hangman()

hangman.print_title()
word: str = input("Guess the word: > ")
if hangman.check_word(word):
    print("You survived!")
else:
    print("You are hanged!")
