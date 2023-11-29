import os
import time
import csv

LOGS_DIR = 'logs'
LOG_FILE = 'tictactoe_log.csv'

# Create 'logs' directory if it doesn't exist
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

class TicTacToeLogger:
    def dict_to_csv(data):
        return ",".join([str(x) for x in data.values()])

    def write_text(text, filename):
        with open(filename, 'a') as f:
            f.write(text + "\n")

    def log_player_move(move_data):
        csv_str = TicTacToeLogger.dict_to_csv(move_data)
        filename = os.path.join(LOGS_DIR, LOG_FILE)
        TicTacToeLogger.write_text(csv_str, filename)
