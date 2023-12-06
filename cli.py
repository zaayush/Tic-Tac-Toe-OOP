
from logic import check_winner
from logger import TicTacToeLogger
import random 
import time
from random import randint

from time import sleep


class TicTacToeGame:
    def __init__(self):
        self.current_player = 'X'
        self.board = self.make_empty_board()
        self.winner = None
        self.logger = TicTacToeLogger()
        self.game_id = None
        

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
        first_move = None
        
        while self.winner is None and any(None in row for row in self.board):
            self.show_board()
            try:
                if self.current_player == 'X':
                    for c in range(10): #For generating 30 log
                        row, col = self.bot_move()
                        sleep(randint(0,1)/10)
                        c =+1
                    '''row, col = self.get_player_input()'''
                    if first_move is None:  # Capture the first move by player 1
                        first_move = (row, col)
                else:
                    row, col = self.bot_move()
                    print(f"Bot (O) chooses: {row}, {col}")

            except ValueError:
                continue

            self.board[row][col] = self.current_player
            self.winner = check_winner(self.board)
            self.switch_player()

        self.show_board()
        self.display_game_result(first_move)


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

 
    def display_game_result(self, first_move):
        if self.winner:
            self.game_id = 1
            print(f"Winner is {self.winner}")

            if choice == '1':
                first_names=('John','Andy','Joe')
                full_name=random.choice(first_names)
                player1, player2 = full_name, 'Bot'
            else:
                player1, player2 = 'Player 1', 'Player 2'
            
            end_time = time.time()  # Record the end time of the game
            game_duration = round(end_time - start_time, 2)
            if self.game_id is not None:
                self.game_id =+ 1
            
            self.logger.log_game_data(self.game_id, self.winner, player1, player2, game_duration, first_move)
            
        else:
            print("It's a tie!")




if __name__ == '__main__':
    print("Welcome to Tic-Tac-Toe!")

   

    while True:
        
        print("Select game mode:")
        print("1. Single Player vs Bot")
        print("2. Double Player")
        for d in range(10): # For generating log data
            choice = "1"
            d =+1
        '''choice = input("Enter your choice (1 or 2): ")'''

        if choice not in ['1', '2']:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        game = TicTacToeGame()

        if choice == '1':
            print("You are playing against the bot!")
            start_time = time.time()  # Record the start time of the game
            game.play_single_player()
          
        else:
            print("You are playing against another player!")
            start_time = time.time()  # Record the start time of the game
            game.play_double_player()

                            

        play_again = input("Do you want to play again? (yes/no): ").lower()

        '''for e in range(10):  # for generating log data
            if e == 10:
                play_again = 'no'
            else:
                play_again = 'yes'
                e =+1
            if e == 10:
                play_again = 'no'''
        if play_again != 'yes':
            break