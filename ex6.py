#more string and text about formatted character
# x is a variable
#string put inside a string
x = "There are %d types of people" % 10
# variable binary is same as string binary
binary = 'binary'
# variable to don't
do_not = "don't"
# added two string together
y = "Those who know %s and those who %s" % (binary, do_not)

#print out the result
print x
print y
#a string put inside a string
print "I said: %r." % x
#a string put inside a string
print "I also said: '%s'." % y

#naming
hilarious = False
#a string put inside a string
joke_evaluation = "Isn't that joke so funny?! %r"

#printing result
#a string put inside a string
print joke_evaluation % hilarious
#naming w and e
w = 'This is the left side of...'
e = 'a string with a right side.'

#print result
print w + e
