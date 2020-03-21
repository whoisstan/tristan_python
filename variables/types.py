#NUMBERS (int) and OPERATIONS

#we are declaring a number variable
tristanBirthYear=2008
#here we are printing it
print(tristanBirthYear)
#we are printing the result of a opperation
print("minus",2020-tristanBirthYear)
print("multiply",tristanBirthYear*5)
print("divive",tristanBirthYear/5)
print("pow",tristanBirthYear ** 99)
print("remainder", 10 % 6)


#STRINGS (str)
#ordered list of characters (abc...)
tristan = "Tristan Wiechers "
print(tristan)

theFirst = tristan + "the first"
print(theFirst)

print(tristan * 2)
print("")

#ARRAY list
soccerTeam = ["brandon","tristan","nash","soren","issac","max","nico","lucas","jacob"]
print(soccerTeam)
print("length", len(soccerTeam) )

for name in soccerTeam:
    print name
    #comparing is if
    if name == "tristan":
        print(u"\u26BD") #soccer symbol
