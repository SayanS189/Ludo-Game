class Player:
    def __init__(self, name):
        self.name = name
        self.pieces = [0, 0, 0, 0]  # Assuming 4 pieces per player

    def roll_dice(self):
        import random
        return random.randint(1, 6)

    def move_piece(self, piece_index, steps):
        if 0 <= piece_index < len(self.pieces):
            self.pieces[piece_index] += steps
            # Add logic to handle piece movement rules here
        else:
            raise IndexError("Invalid piece index")