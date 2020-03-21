
#Tristan Assignments 3/21/2330

names = ["oma","tristan","ronaldo","messi","guacho","liam","pig","dog"]


# 1. print each name and when it's name is dog print "woof" as well
for name in names:
    print name
  
    if name == "dog":
        print("woof") 

# 2. print the length of the array
print("length", len(names) )
# 3. add "takeshi" to the list
print(names + ["takeshi"])
names = names + ["takeshi"]
# 4. print each name and when it's name is takeshi print "kovac" as well  
for name in names:
    print name
  
    if name == "takeshi":
       print("++++kovac++++")

# 5. print the length of the array
print("length", len(names) )

