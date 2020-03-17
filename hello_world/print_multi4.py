#loading a library
import sys



# reading the instructions from the commandline
# example:  python print_multi4.py xyz 10000
content = sys.argv[1] #"xyz"
amount = int(sys.argv[2]) # 10000

# the variable to print out hence output
output = ""

#repeat the statement inside the loop 10000 times
for x in range(0, amount):
    #appending the value of content to output
    #this is repeated
    output = output + content + " "

#this only printed once
print(output)    