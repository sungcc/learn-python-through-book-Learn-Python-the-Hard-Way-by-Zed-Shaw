# printing printing to go

formatter = "%r %r %r %r"

#printing the 4 input
print formatter % (1, 2, 3, 4)

#printing the string with formatter
print formatter % ('one', 'two', 'three', 'four')

#printing the boolean
print formatter % (True, False, False, True)

#printing formatter with formatter
print formatter % (formatter, formatter, formatter, formatter)

#printing long string
print formatter % ("I had this thing.", "That you could type up right", "But it didn't sing.", "So I said goodnight.")
