
from random import random

def random_number(range):
	"""creates a random integer between 0 and range-1"""
	return int(random()*range)

def prompt(message):
    response = raw_input(message)
    return response

max = 99
score = 0



while True:
    
    print ("Your current score: "+str(score))
    user_response = prompt("Guess the exact number between 0 and 10!") 
    if( user_response == "q" ):
        break
    else:
        #ignore that try

        try:
            user_number = int(user_response)
            game_number = random_number(max)
            print("the game number was "+str(game_number))
            #cheating
            if ( user_number > max):
                print( "are you a cheetah?")
            #winning    
            elif ( user_number == game_number):
                print( "you are too smart for me :)")
                score = score + 10             
            #loosing    
            else:
                print ("gotcha [O\\\\\[========================>>")
                score = score - 1
        #ignore that except    
        except ValueError:
            #Handle the exception
            print 'I said a number!'
        

   