''' def write_text (text,filename):
 
    with open(filename, 'w') as f:
        f.write(text +"\n")
        print ("Finished Writing")
 
write_text("Hello,World" , "hello.txt") '''
 
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
 
    }
def dict_to_csv(data):
    """"
        input:
 
        data -> dictionary
       
        output:
 
        csv_str -> a valid csv row, i.e 1,ian,uw
   
    """
    [str(x) for x in data.values()]
 
 
dict_to_csv({"Naame" : "ian", "score" : 123})
 
   
    for value in data.values():
