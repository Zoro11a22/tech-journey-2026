# A simple time based greeter

from datetime import datetime as dt

def greeter():

    time = dt.now().hour

    if( 4 <= time <= 11):
        return "Good Morning!"
    elif( 12 <= time <= 16 ):
        return "Good Afternoon!"
    elif( 17 <= time <= 19 ):
        return "Good Evening!"
    else:
        return "Good Night!"
