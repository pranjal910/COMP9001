import sys
import random
from player import Player
from utils import print_intro, print_header, color, slow_print
from rooms import LionRoom, SerpentRoom, MirrorRoom, LibraryRoom, MusicRoom

class Game:
    def __init__(self):
        self.player = Player()
        self.room_digit_map = {}
        self.room_visit_order = []
        self.rooms = [
            ("Lion Room", LionRoom),
            ("Serpent Room", SerpentRoom),
            ("Mirror Room", MirrorRoom),
            ("Library Room", LibraryRoom),
            ("Music Room", MusicRoom)
        ]

    def assign_digits(self):
        digits = random.sample([str(i) for i in range(1, 10)], len(self.rooms))
        room_keys = ['lion', 'serpent', 'mirror', 'library', 'music']
        self.room_digit_map = dict(zip(room_keys, digits))

    def choose_rooms(self):
        print_header("\U0001f3f0 Choose 3 Rooms to Explore")
        visited = set()

        while len(visited) < 3 and self.player.lives > 0:
            print(color("Available Rooms:", fg='cyan', style='bold'))
            for idx, (name, _) in enumerate(self.rooms, 1):
                if idx not in visited:
                    print(f"{idx}. {name}")
            print(color("0. Exit Game", fg='red'))

            choice = input(color("Enter room number (or 0 to exit): ", fg='blue')).strip()

            if choice == '0':
                print(color("\n\U0001f44b Exiting the game. Come back soon!", fg='magenta', style='bold'))
                sys.exit()

            if choice.isdigit() and 1 <= int(choice) <= len(self.rooms) and int(choice) not in visited:
                idx = int(choice) - 1
                visited.add(int(choice))
                room_name, room_cls = self.rooms[idx]
                room_key = room_cls.__name__.replace("Room", "").lower()
                room = room_cls(self.player, self.room_digit_map[room_key])
                success = room.enter()
                if success:
                    self.room_visit_order.append(room_key)
            else:
                print(color("\u274c Invalid or already visited.", fg='red'))

    def final_challenge(self):
        print_header("\U0001f6aa The Final Vault")
        slow_print(color("You must enter the 3-digit escape code...", fg='yellow'))
        correct_code = ''.join([self.room_digit_map[r] for r in self.room_visit_order])
        final_input = input(color("Enter the code: ", fg='blue')).strip()

        if final_input == correct_code:
            print(color("\U0001f389 The vault opens! You have escaped!", fg='green', style='bold'))
        else:
            self.player.lose_life()
            if self.player.lives > 0:
                self.final_challenge()

    def start(self):
        self.assign_digits()
        print_intro()
        self.choose_rooms()
        if self.player.lives > 0:
            self.final_challenge()
