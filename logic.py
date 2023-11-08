def check_winner(board):
    # check rows
    #    ['X', 'X', 'X'], -> set(['X', 'X', 'X']) -> {'X'}
    #    ['O', 'X', 'O'], -> set(['O', 'X', 'O']) -> {'X', 'O'}
    #    ['O', 'O', 'X'],
    for row in board:
        if len(set(row)) == 1:
            return row[0]

    # check columns
    #    ['X', 'X', 'X'],
    #    ['O', 'X', 'O'],
    #    ['O', 'O', 'X'],
    # how to index -> board[row][column]
    # column_idxs = [[0,0], [1,0], [2,0]]
    # column_idxs = [[0,1], [1,1], [2,1]]
    for i in range(len(board)):
        # len(board) -> 3
        column = [board[j][i] for j in range(len(board))]
        # column => ['X', 'O', 'O']
        # column => ['X', 'X', 'O]
        if len(set(column)) == 1:
            return board[0][i]

    # check diagonals
    # check columns
    #    ['X', 'X', 'X'],
    #    ['O', 'X', 'O'],
    #    ['O', 'O', 'X'],
    # how to index -> board[row][column]
    # idx -> [[0,0], [1,1], [2, 2]]
    top_left_to_bottom_right = [board[i][i] for i in range(len(board))]
    if len(set(top_left_to_bottom_right)) == 1:
        return board[0][0]

    # check diagonals
    # check columns
    #    ['X', 'X', 'X'],
    #    ['O', 'X', 'O'],
    #    ['O', 'O', 'X'],
    # how to index -> board[row][column]
    # idx -> [[0,2], [1,1], [2, 0]]
    top_right_to_bottom_left = [board[i][len(board)-i-1] for i in range(len(board))]
    if len(set(top_right_to_bottom_left)) == 1:
        return board[0][len(board)-1]
    
    
    flat_board = []
    for row in board:
        flat_board.extend(row)

    if not None in flat_board:
        return"draw"
    return None
    return "Draw"

