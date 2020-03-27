# 1.) create a random number between 0 and 99
# 2.) ask the user to guess the number
#     - if the user is too high tell him he is to high, reward -1
#     - if the user is too low tell him he is to low, 
#     - if user matches tell him yeah



    
from random import random

def random_number(range):
	"""creates a random integer between 0 and range-1"""
	return int(random()*range)

def prompt(message):
    response = raw_input(message)
    return response

max = 100
reward = 10 

game_number = random_number(max)

print("Guess the exact number between 0 and 100! ")

while True:
    
   
    user_response = prompt("Your number: ") 
    if( user_response == "q" ):
        break
    else:
        try:
            user_number = int(user_response)          
            #if user number was bigger tha the original it says:
            if ( user_number > game_number):
                print("too big")
                reward = reward - 1
            #if user number was smaller tha the original it says:
            elif ( user_number < game_number):
                print( "too small") 
                reward = reward - 1            
            #winning    
            
            else:
                print( "you are too smart for me :)")                
                print ("Your current score: "+str(reward))
                break
            
            #ignore that except    
        except ValueError:
            #Handle the exception
            print 'I said a number!'
        