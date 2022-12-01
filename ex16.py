#import modules
from sys import argv

script, filename = argv
#give a guide, and display the filename
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
#let user input to decide
raw_input("?")
#filename is decided when user input the script
print "Opening the file..."
target = open(filename, 'w')
#format the txt file first
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
#adding 3 lines with user input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to file."
#user input
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
# close the file
