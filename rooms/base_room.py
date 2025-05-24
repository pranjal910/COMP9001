from utils import print_header, color

class BaseRoom:
    def __init__(self, player, digit):
        self.player = player
        self.digit = digit

    def enter(self):
        raise NotImplementedError("Each room must implement its own logic")
