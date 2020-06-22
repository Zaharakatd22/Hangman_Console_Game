class Hangman:
    def __init__(self, title: str = "H A N G M A N", announcement: str = "The game will be available soon."):
        self.title = title
        self.announcement = announcement

    def print_title(self):
        print(self.title)

    def print_announce(self):
        print(self.announcement)


hangman = Hangman()

hangman.print_title()
hangman.print_announce()