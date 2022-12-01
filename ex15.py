#reading files
#import a small part of whole modules
from sys import argv
#giving argv our script
script, filename = argv
#assign txt to a read a file
txt = open(filename)
#here printing a line  our txt name
print "Here's your file %r:" % filename
# print out the text inside the input file
print txt.read()
#print a line to guide
print "Type the filename again:"
#assign variable to raw_input
file_again = raw_input("> ")
#there is two way to output text from file
txt_again = open(file_again)
#print the text out
print txt_again.read()

#this time I got no error message
#but not output all the txt from ex15_sample.txt
#I found out I didn't save the file .. how stupid I am
