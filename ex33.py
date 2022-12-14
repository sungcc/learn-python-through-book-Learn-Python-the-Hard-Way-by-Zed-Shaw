i = 0
number = []

while i > 0:
    print "At the top i is %d" % i
    number.append(i)

    i += 2
    print "Numbers now: ", number
    print " At the bottom i is %d" % i

print "The number: "

for num in number:
    print num
