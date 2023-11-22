''' def write_text (text,filename):
 
    with open(filename, 'w') as f:
        f.write(text +"\n")
        print ("Finished Writing")
 
write_text("Hello,World" , "hello.txt") '''
"""
play =
    {
        "symbol": "x"
        "move_count" : "1"
        "move" : "1.2"
        " time_spent" : "60"
 
    },
    {
        "symbol": "x"
        "move_count" : "1"
        "move" : "1.2"
        " time_spent" : "60"
 
    }"""
 
def dict_to_csv(data):
    """"
        input:
 
        data -> dictionary
       
        output:
 
        csv_str -> a valid csv row, i.e 1,ian,uw
   
    """
    return ",".join([str(x) for x in data.values()])
 
move_data = {
    'symbol' :'X',
    'duration_seconds' : 60,
    'move' : 2,
}
 
 
def ask_player_move(symbol):
 
    """ Input:
            move -> integer between 0 and 8
        Output:
            True if move success False is move is invalid
    """
    move_data = {}
    move_start_time = time.time()
    move = input("Please Enter a Move, valid move is between 0 and 8 ")
    move_data['symbol'] = symbol
    move_data['move'] = move
    move_done_time = time.time()
    move_data [' duration_seconds '] = move_done_time - move_start_time
 
    print(move_data)
    csv_str = dict_to_csv()
    write_text_to_file(csv_str)
 
 
ask_player_move = ('X')
print(move_data)
"""
move_data = {
"game_id": <unique_id>
}
"""
import random
import time
def game():
    game_id = time.time()
    while True:
        ask_player_for_move()
"""
generate fake game play data
"""

data = {
    "game_id": "",
    "symbol": "",
    "duration": "",
    "move": "",
    "is_winner": "",
}