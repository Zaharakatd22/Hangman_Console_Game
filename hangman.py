import random


class Hangman:
    def __init__(self, title: str = "H A N G M A N",
                 announcement: str = "The game will be available soon.",
                 guessed_words=None):
        if guessed_words is None:
            guessed_words = ["python", "java", "kotlin", "javascript"]
        self.title: str = title
        self.announcement: str = announcement
        self.guessed_words = guessed_words
        self.guessed_word: str = ""

    def print_title(self):
        print(self.title)

    def print_announce(self):
        print(self.announcement)

    def make_guessed_word(self):
        self.guessed_word = random.choice(self.guessed_words)  # Random choice guessed word

    def check_word(self, user_word: str) -> bool:
        return user_word == self.guessed_word

    def hint_word(self) -> str:
        return self.guessed_word[:3] + "-" * (len(self.guessed_word) - 3)


hangman = Hangman()

hangman.print_title()
hangman.make_guessed_word()
hint_word: str = hangman.hint_word()
word: str = input(f"Guess the word {hint_word} : > ")
if hangman.check_word(word):
    print("You survived!")
else:
    print("You are hanged!")
