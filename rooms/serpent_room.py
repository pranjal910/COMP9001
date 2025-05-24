from rooms.base_room import BaseRoom
from utils import print_header, color
import random

class SerpentRoom(BaseRoom):
    def enter(self):
        print_header("\U0001f40d Room of the Serpent")
        print("Three levers lie before you. Only one is safe.")

        safe = str(random.randint(1, 3))
        attempts = 2
        while attempts > 0:
            choice = input(color("Choose a lever (1, 2, 3): ", fg='blue')).strip()
            if choice == safe:
                print(color(f"\u2705 Safe! A trapdoor opens with a brass number: {self.digit}.", fg='green'))
                return True
            else:
                attempts -= 1
                self.player.lose_life()
        print(color("Poison darts shoot from the walls... You barely escape.", fg='red'))
        return False
