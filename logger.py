import csv
import os
import datetime

class TicTacToeLogger:
    def __init__(self):
        self.log_file_path = 'logs/game_log.csv'
        self.create_log_file()

    def create_log_file(self):
        if not os.path.exists('logs'):
            os.makedirs('logs')

        if not os.path.exists(self.log_file_path):
            with open(self.log_file_path, 'w', newline='') as csvfile:
                fieldnames = ['Player 1', 'Player 2', 'Winner', 'Game Duration', 'Timestamp']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

    def log_game_result(self, player1, player2, winner, game_duration):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open(self.log_file_path, 'a', newline='') as csvfile:
            fieldnames = ['Player 1', 'Player 2', 'Winner', 'Game Duration', 'Timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({
                'Player 1': player1,
                'Player 2': player2,
                'Winner': winner,
                'Game Duration': game_duration,
                'Timestamp': timestamp
            })

    def display_statistics(self):
        with open(self.log_file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header
            total_games = 0
            player1_wins = 0
            player2_wins = 0
            draws = 0

            for row in reader:
                total_games += 1
                if row[2] == 'X':
                    player1_wins += 1
                elif row[2] == 'O':
                    player2_wins += 1
                else:
                    draws += 1

            print(f"\nStatistics:\nTotal Games: {total_games}\nPlayer 1 Wins: {player1_wins}\nPlayer 2 Wins: {player2_wins}\nDraws: {draws}")


