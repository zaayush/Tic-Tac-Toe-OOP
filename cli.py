
from logic import check_winner
from logger import TicTacToeLogger
import random
import datetime

class TicTacToeGame:
    def __init__(self):
        self.current_player = 'X'
        self.board = self.make_empty_board()
        self.winner = None

    def make_empty_board(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def get_player_input(self, player_input=None):
        prompt = f"Player {self.current_player}, please input your move (row, col): \n"
        while True:
            try:
                if player_input is None:
                    player_input = input(prompt)
                    row, col = map(int, player_input.split(','))
                # Check if the spot is already taken
                if self.board[row][col] is not None:
                    raise ValueError("Place already filled. Try again")
                    player_input = None
                    break
                return row, col
            except ValueError as e:
                print(f"Invalid input: {e}\n")
                player_input = None
                continue
                
    def show_board(self):
        board2 = [[' ' if cell is None else cell for cell in row] for row in self.board]

        print("\n")
        print("\t     |     |")
        print(f"\t  {board2[0][0]}  |  {board2[0][1]}  |  {board2[0][2]}")
        print('\t_____|_____|_____')
        print("\t     |     |")
        print(f"\t  {board2[1][0]}  |  {board2[1][1]}  |  {board2[1][2]}")
        print('\t_____|_____|_____')
        print("\t     |     |")
        print(f"\t  {board2[2][0]}  |  {board2[2][1]}  |  {board2[2][2]}")
        print("\t     |     |")
        print("\n")

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_single_player(self):
            while self.winner is None and any(None in row for row in self.board):
                self.show_board()
                try:
                    if self.current_player == 'X':
                        row, col = self.get_player_input()
                    else:
                        row, col = self.bot_move()
                        print(f"Bot (O) chooses: {row}, {col}")

                except ValueError:
                    continue

                self.board[row][col] = self.current_player
                self.winner = check_winner(self.board)
                self.switch_player()

            self.show_board()
            self.display_game_result()


    def bot_move(self):
        # Simple random move for the bot
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]
        return random.choice(available_moves)


    def play_double_player(self):
        while self.winner is None and any(None in row for row in self.board):
            self.show_board()
            row, col = self.get_player_input()               
            self.board[row][col] = self.current_player
            self.winner = check_winner(self.board)
            self.switch_player()

        self.show_board()
        self.display_game_result()

    def display_game_result(self):
        if self.winner:
            print(f"Winner is {self.winner}")
        else:
            print("It's a tie!")
    
    # Code for logging data
    def display_game_result(self):
        if self.winner:
            print(f"Winner is {self.winner}")
            log_data = {'winner': self.winner}
            
        else:
            print("It's a tie!")

if __name__ == '__main__':
    print("Welcome to Tic-Tac-Toe!")

    logger = TicTacToeLogger()

    while True:
        print("Select game mode:")
        print("1. Single Player vs Bot")
        print("2. Double Player")
        choice = input("Enter your choice (1 or 2): ")

        if choice not in ['1', '2']:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        game = TicTacToeGame()

        if choice == '1':
            print("You are playing against the bot!")
            start_time = datetime.datetime.now()
            game.play_single_player()
            end_time = datetime.datetime.now()
            game_duration = end_time - start_time
            logger.log_game_result("Player 1", "Bot", game.winner, game_duration)

        else:
            print("You are playing against another player!")
            start_time = datetime.datetime.now()
            game.play_double_player()
            end_time = datetime.datetime.now()
            game_duration = end_time - start_time
            logger.log_game_result("Player 1", "Player 2", game.winner, game_duration)

        logger.display_statistics()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break



