from logic import check_winner

def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

# Reminder to check all the tests
def get_player_input(current_player):
    prompt = f"player {current_player}, Please input your move \n"
    player_input = input(prompt)
    row_col_list = player_input.split(',')
    row, col = [int(x) for x in row_col_list]    
    return row, col

def show_board(board):
    print(board[0])
    print(board[1])
    print(board[2])

def switch_player(current_player):
    if current_player == "X":
        return "O"
    return "X"

if __name__ == '__main__':
    current_player = 'X'
    board = make_empty_board()
    """board = [
        ["O", "X", "O"],
        ["X", "X", "O"],
        ["O", "O", "X"]
    ]"""
    
    winner = None

    while winner is None:
        show_board(board)
        try:
            row, col = get_player_input(current_player)
        except ValueError:
            print("Invalid Input, try again\n")
            continue
        
        board[row][col] = current_player
        winner = check_winner(board)
        current_player = switch_player(current_player)

    show_board(board)
    print(f"winner is {winner}")
