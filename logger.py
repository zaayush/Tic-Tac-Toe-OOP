import csv
import os
import datetime
import pandas as pd
import numpy as np

class TicTacToeLogger:
    def __init__(self):
        self.log_directory = "./logs"
        self.log_file_path = os.path.join(self.log_directory, "updated5_game_data.csv")
        self.create_log_directory()
        self.create_log_file()

    def create_log_directory(self):
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

    def create_log_file(self):
        if not os.path.isfile(self.log_file_path):
            with open(self.log_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Game ID", "Winner", "Player 1", "Player 2", "Game Duration", "First Move", "Timestamp"])

    def log_game_data(self, game_id, winner, player1, player2, game_duration, first_move):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(first_move, (tuple, list)):
            first_move_list = first_move
        elif isinstance(first_move, np.ndarray):
            first_move_list = first_move.tolist()
        else:
            first_move_list = None

        game_data = {
            "Game ID": game_id,
            "Winner": winner,
            "Player 1": player1,
            "Player 2": player2,
            "Game Duration": game_duration,
            "First Move": first_move_list,
            "Timestamp": timestamp
        }
        self.append_to_csv([game_data])  # Pass a list of dictionaries

    def append_to_csv(self, game_data_list):
        df = pd.DataFrame(game_data_list)
        df.to_csv(self.log_file_path, mode='a', header=False, index=False)

# Example of usage:
logger = TicTacToeLogger()
logger.log_game_data(1, "X", "PlayerA", "PlayerB", 30, (1, 0, 0, 0, 0, 0, 0, 0, 0))  # Replace this tuple with your actual data
