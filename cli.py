from logic import check_winner
import random

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

    def get_player_input(self):
        prompt = f"Player {self.current_player}, please input your move (row, col): \n"
        while True:
            try:
                player_input = input(prompt)
                row, col = map(int, player_input.split(','))
                return row, col
            except ValueError:
                print("Invalid input, try again\n")

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
            try:
                row, col = self.get_player_input()
                if self.board[row][col] != None:
                    print("Place already filled. Try again!!")
                    continue
            except ValueError:
                continue

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


    def play(self):
        while self.winner is None:
            self.show_board()
            try:
                row, col = self.get_player_input()
                #Check if place already filled
                if self.board[row][col] != None:
                    print("Place already filled. Try again!!")
                    row, col = self.get_player_input()
                    continue
            except ValueError:
                continue

            self.board[row][col] = self.current_player
            self.winner = check_winner(self.board)
            self.switch_player()

        self.show_board()
        print(f"Winner is {self.winner}")


'''if __name__ == '__main__':
    game = TicTacToeGame()
    game.play()'''

if __name__ == '__main__':
    print("Welcome to Tic-Tac-Toe!")

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
            game.play_single_player()
        else:
            print("You are playing against another player!")
            game.play_double_player()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break


