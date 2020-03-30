import sys
from random import random
from os import system

#function
def random_number(range):
	"""creates a random integer between 0 and range-1"""
	return int(random()*range)

def prompt(message,range):
    response = raw_input(message)
    if(response == "q" ):
        sys.exit()
    else:
        try:
            user_number = int(response)   
            if(user_number>=range or range <0):
                print("wrong input")
                return prompt(message,range)
            
            return  user_number                      
        except ValueError:
            print("wrong input")
            return prompt(message,range)      

#init
user_health_points = 10 
com_health_points = 10

round = 1

#logic 
while True:
        
    print("******")
    print("Round "+str(round))
    print("******")    
    round = round + 1

    user_attack_position  = prompt("Your attack position(0,1,2,3): ",4) 
    user_defense_position = prompt("Your defense position(0,1,2): ",3)

    com_attack_position = random_number(4)
    com_defense_position = random_number(3)

    print ("com attack position: "+str(com_attack_position))
    print ("com defense position: "+str(com_defense_position))

    #its going to determine if user attack was succesful
    if(user_attack_position == 3):
        user_health_points = user_health_points +1
        print("User ate a healthy mushroom")    
    elif (user_attack_position != com_defense_position):
        com_health_points = com_health_points - 1
        system('say you hurt me!')
        if (com_health_points == 0 ):        
            print( open('state/com_dead.txt', 'r').read())           

    if(com_attack_position == 3):
        com_health_points = com_health_points +1
        print("Computer ate a healthy mushroom")

    elif (com_attack_position != user_defense_position):
        user_health_points = user_health_points -1          
        system('say you suck')
        if (user_health_points == 0 ):        
            print( open('state/user_dead.txt', 'r').read())   
          

    print ("com health: "+str(com_health_points))
    print ("user health: "+str(user_health_points))

    print(" ")

    if (com_health_points == 0 or user_health_points == 0):
        break