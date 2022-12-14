# Name, Variables, Code, Functions

# Functions do three things:
#  1. They name pieces of code the way variables name strings and numbers.
#  2. They take arguments the way your scripts take argv.


#this one is like your scripts with argv

def print_two(*args):
        arg1, arg2 = args
        print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *argv is actually pointless, we can just do This
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this one takes no argument
def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
