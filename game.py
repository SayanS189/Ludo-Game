class Game:
    def __init__(self):
        self.players = []
        self.board = None
        self.current_turn = 0

    def start_game(self):
        self.setup_board()
        self.setup_players()
        self.game_loop()

    def setup_board(self):
        from board import Board
        self.board = Board()
        self.board.setup()

    def setup_players(self):
        from player import Player
        num_players = int(input("Enter number of players (2-4): "))
        for i in range(num_players):
            name = input(f"Enter name for player {i + 1}: ")
            self.players.append(Player(name))

    def game_loop(self):
        while True:
            self.take_turn()
            if self.check_winner():
                break

    def take_turn(self):
        player = self.players[self.current_turn]
        print(f"{player.name}'s turn.")
        player.roll_dice()
        # Logic for moving pieces would go here
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def check_winner(self):
        for player in self.players:
            if player.has_won():
                print(f"{player.name} wins!")
                return True
        return False