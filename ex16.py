# Importing necesary modules from packages
from sys import argv

script, filename = argv

print "We're going to erase %r " % filename
print "Press Ctrl-C to stop that."
print "Else press enter to continue with the operation"

# Waiting for user response
raw_input('?')

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you to enter 3 more lines"

line1 = raw_input("line 1 : ")
line2 = raw_input("line 2 : ")
line3 = raw_input("line 3 : ")

print "Writing them into the file..."

# Writing in single line without repetition
target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

print "And finally we close it."
target.close()
