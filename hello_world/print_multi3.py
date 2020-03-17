# declaring a variable called content
content = "Hello World "
# the variable to print out hence output
output = ""

#repeat the statement inside the loop 10000 times
for x in range(0, 10000):
    #appending the value of content to output
    #this is repeated
    output = output + content

#this only printed once
print(output)    