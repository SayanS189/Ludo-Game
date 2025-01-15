class Board:
    def __init__(self):
        self.board_size = 15  # Default size of the board, adjust as needed
        self.board = self.setup_board()

    def setup_board(self):
        # Initialize the board layout as a 15x15 grid (or modify as per requirement)
        return [[" " for _ in range(self.board_size)] for _ in range(self.board_size)]

    def display(self):
        # Display the current state of the board
        print("\nBoard Layout:")
        for row in self.board:
            print("|".join(row))
            print("-" * (self.board_size * 2 - 1))

    def move_piece(self, player, piece, steps):
        # Logic to move a player's piece on the board
        # Ensure we have the position for the piece, for example: player.pieces[piece]
        # Assuming the player has a list of pieces represented by coordinates (row, col)
        piece_position = player.pieces[piece]
        current_row, current_col = piece_position

        # Calculate new position after moving
        new_row, new_col = current_row, current_col + steps  # Horizontal movement example

        # Check if new position is within board limits and not occupied
        if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size:
            # Update the board with the player's piece (ensure to clear the old position)
            self.board[current_row][current_col] = " "
            self.board[new_row][new_col] = player.name[0]  # Use first letter of player's name

            # Update the piece's position in player's piece list
            player.pieces[piece] = (new_row, new_col)
        else:
            print("Invalid move. Try again.")

    def reset_board(self):
        # Reset the board for a new game
        self.board = self.setup_board()
