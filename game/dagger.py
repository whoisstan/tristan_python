
from random import random

def random_number(range):
	"""creates a random integer between 0 and range-1"""
	return int(random()*range)

def prompt(message):
    response = raw_input(message)
    return response

max = 5
score = 0


# 1.) show the user the random number
# 2.) if the user wins inrease score by 3
# 3.) if the user wins looses decrease score by 1
# 4.) print score before asking him for the next choice

while True:
    user_response = prompt("Guess bigger number between 0 and 4!") 
    if( user_response == "q" ):
        break
    else:
        #ignore that try
        try:
            user_number = int(user_response)
            game_number = random_number(max)
            #win
            if ( user_number > max):
                print( "are you a cheetah?")
            elif ( user_number > game_number):
                print( "you are too smart for me :)")                
            else:
                print ("gotcha [O\\\\\[========================>>")
        #ignore that except    
        except ValueError:
            #Handle the exception
            print 'I said a number!'       
            
    
