# Importing necesary modules from packages
from sys import argv

script, filename = argv

print "We're going to erase %r " % filename
print "Press Ctrl-C to stop that."
print "Else press enter to continue with the operation"

# Waiting for user response
raw_input('?')

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you to enter 3 more lines"

line1 = raw_input("line 1 : ")
line2 = raw_input("line 2 : ")
line3 = raw_input("line 3 : ")

print "Writing them into the file..."

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "And finally we close it."
target.close()
