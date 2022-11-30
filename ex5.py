#here you can see more variable and printing

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
heightInCM = height * 2.54
weight = 180 #lbs
weightInKG = weight / 2.2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
print "print no matter what %r" % weightInKG
print "let's talk about %s" % name
print "he's %f cm tall" % round(heightInCM)
print "he's %f kg heavy" % weightInKG
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" %(eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

#this line is tricky, try to git it exactly right

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
