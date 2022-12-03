#import sys modules argv functions
from sys import argv
#the script need one argument
script, input_file = argv
#print_all function create
def print_all(f):
    print f.read() #read whole document

#rewind function create
def rewind(f):
    f.seek(0) #point to the first line of file

#define print_a_line function
def print_a_line(line_count, f):
    print line_count, f.readline()

#running the function open the input file Name
current_file = open(input_file)

print "First let's print the whole file:\n"
#call print_all
print_all(current_file)

print "Now let's rewind, kind of like a tape."
#call rewind function
rewind(current_file)
#call third function
print "Let's print three lines:"
#calling third function, the argument is a variable
current_line = 1
print_a_line(current_line, current_file)
# combine variable with + 
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
