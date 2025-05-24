from rooms.base_room import BaseRoom
from utils import print_header, color

class MirrorRoom(BaseRoom):
    def enter(self):
        print_header("\U0001faaE Room of the Mirror")
        print("A message is etched: '379'. It appears reversed.")
        print(color("HINT: Imagine looking from behind the mirror.", fg='yellow'))

        attempts = 2
        while attempts > 0:
            guess = input(color("What number do you see when it's mirrored? ", fg='blue')).strip()
            if guess == "973":
                print(color(f"\u2705 You solved it! The number {self.digit} is etched behind the glass.", fg='green'))
                return True
            else:
                attempts -= 1
                self.player.lose_life()
        print(color("The mirror fogs up and shows only your failure.", fg='red'))
        return False
