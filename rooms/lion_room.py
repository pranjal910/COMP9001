from rooms.base_room import BaseRoom
from utils import print_header, color

class LionRoom(BaseRoom):
    def enter(self):
        print_header("\U0001f981 Room of the Lion")
        print("Riddle: " + color("What comes once in a minute, twice in a moment, but never in a thousand years?", fg='magenta'))

        attempts = 2
        while attempts > 0:
            answer = input(color("Your answer: ", fg='blue')).strip().lower()
            if answer == "m":
                print(color(f"\u2705 Correct! You find a plate with the number {self.digit}.", fg='green'))
                return True
            else:
                attempts -= 1
                self.player.lose_life()
        print(color("The lion roars and you flee in panic...", fg='red'))
        return False
