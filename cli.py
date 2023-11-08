from logic import check_winner
# Function to print Tic Tac Toe
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
    '''elif player_input == 9:
        row = '0'
        col = '2'
    elif player_input == 4:
        row, col = '1','0'
    elif player_input == 5:
        row, col = '1','1'
    elif player_input == 6:
        row, col = '1','2'
    elif player_input == 1:
        row, col = '2','0'
    elif player_input == 2:
        row, col = '2','1'
    elif player_input == 3:
        row, col = '2','2'
    '''
    
    

def show_board(board):
    # For printing blank space instead of None
    board2 = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
    for a in range(3):
        for b in range(3):
            if board[a][b] == None:
                board2[a][b] = ' '
            else: 
                board2[a][b] = board[a][b]

    # Printing Pattern with board values
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


def switch_player(current_player):
    if current_player == "X":
        return "O"
    return "X"

if __name__ == '__main__':
    current_player = 'X'
    board = make_empty_board()

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
