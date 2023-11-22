from logic import check_winner
import pytest
from cli import TicTacToeGame

def test_game_initialization():
    game = TicTacToeGame()
    assert game.board == [[None, None, None], [None, None, None], [None, None, None]]
    assert game.current_player == 'X'
    assert game.winner is None

def test_player_assignment():
    game = TicTacToeGame()
    assert game.current_player == 'X'
    game.switch_player()
    assert game.current_player == 'O'
    game.switch_player()
    assert game.current_player == 'X'

def test_valid_moves():
    game = TicTacToeGame()
    assert game.make_empty_board() == [[None, None, None], [None, None, None], [None, None, None]]
    row, col = game.get_player_input()
    assert (row, col) in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

def test_invalid_moves():
    game = TicTacToeGame()
    game.board[0][0] = 'X'
    with pytest.raises(ValueError):
        game.get_player_input()

def test_game_winner():
    game = TicTacToeGame()
    game.board = [['X', 'O', 'X'], [None, 'O', 'O'], ['X', None, 'X']]
    assert check_winner(game.board) == 'X'

def test_draw_game():
    game = TicTacToeGame()
    game.board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
    assert check_winner(game.board) is None

# Add more test cases as needed

if __name__ == '__main__':
    pytest.main(['test.py'])
