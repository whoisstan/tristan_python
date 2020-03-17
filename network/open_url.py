import urllib

link = "http://www.merkwelt.com/people/stan"

f = urllib.urlopen(link)
myfile = f.read()

print(myfile)