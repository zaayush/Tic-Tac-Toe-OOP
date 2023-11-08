from logic import check_winner

boards = [
    [
        ['O', '1', 'O'],
        ['O', '1', 'O'],
        ['O', 'O', '1'],
    ],
    [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ],
    [
        ['X', 'O', 'X'],
        ['O', 'X', 'X'],
        ['O', 'X', 'O'],
    ],
]

for idx, board in enumerate(boards):
    winner = check_winner(board)
    print(f"{idx}: {winner}")# Test Scenarios
