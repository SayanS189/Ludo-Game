def main():
    print("Welcome to Ludo Game!")
    
    # Initialize game components
    from board import Board
    from player import Player
    from game import Game

    # Create game board
    game_board = Board()
    game_board.setup()

    # Create players
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    
    # Initialize game
    ludo_game = Game(game_board, [player1, player2])
    
    # Start game loop
    while not ludo_game.is_game_over():
        ludo_game.play_turn()

    print("Game Over! Thank you for playing.")

if __name__ == "__main__":
    main()