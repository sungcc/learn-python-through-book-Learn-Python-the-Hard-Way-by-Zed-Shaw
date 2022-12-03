from sys import argv
# new modules os
from os.path import exists
#need to input two argument
script, from_file, to_file = argv
#two argument to string
print "Copying from %s to %s." % (from_file, to_file)

#we could do these two on one line too, how?
#open a file first argv
in_file = open(from_file)
#read the first file assign to indata
indata = in_file.read()
#printing the bytes
print "The input file is %d bytes long" % len(indata)
#checking the second argument file here or not
print "Does the output file exist? %r" % exists(to_file)
#giving choice to user to continue
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

#write data to second file
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done"
#closing file
out_file.close()
in_file.close()
