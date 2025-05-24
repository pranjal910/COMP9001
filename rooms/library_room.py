from rooms.base_room import BaseRoom
from utils import print_header, color

class LibraryRoom(BaseRoom):
    def enter(self):
        print_header("\U0001f4da Library of Ciphers")
        print("You find an old scroll with the word: 'mjhiu'")
        print(color("HINT: Each letter is shifted one step forward in the alphabet.", fg='yellow'))

        attempts = 2
        while attempts > 0:
            answer = input(color("Decode the word and enter it: ", fg='blue')).strip().lower()
            if answer == "light":
                print(color(f"\u2705 You cracked the code! A glowing book reveals: {self.digit}.", fg='green'))
                return True
            else:
                attempts -= 1
                self.player.lose_life()
        print(color("The books rearrange themselves into unreadable symbols.", fg='red'))
        return False
