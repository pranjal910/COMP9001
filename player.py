import sys
from utils import color

class Player:
    def __init__(self):
        self.lives = 3

    def lose_life(self):
        self.lives -= 1
        if self.lives > 0:
            print(color(f"\u26a0\ufe0f Incorrect! You have {self.lives} {'life' if self.lives == 1 else 'lives'} left.\n", fg='yellow'))
        else:
            self.game_over()

    def game_over(self):
        print(color("\n\U0001f480 GAME OVER \U0001f480", fg='red', style='bold'))
        print("You have run out of lives. The vault remains sealed.")
        sys.exit()
