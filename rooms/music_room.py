from rooms.base_room import BaseRoom
from utils import print_header, color

class MusicRoom(BaseRoom):
    def enter(self):
        print_header("\U0001f3b5 Room of Echoes")
        print("You hear the notes: Do, Re, Mi, ?, So")
        print(color("HINT: It's a standard musical scale.", fg='yellow'))

        attempts = 2
        while attempts > 0:
            answer = input(color("What note is missing? ", fg='blue')).strip().lower()
            if answer == "fa":
                print(color(f"\u2705 That’s right! A musical rune shows the number {self.digit}.", fg='green'))
                return True
            else:
                attempts -= 1
                self.player.lose_life()
        print(color("The echoes turn dissonant and fade into silence.", fg='red'))
        return False
