# Importing necessary modules from packages

from sys import argv

script, file_name = argv

 # Creating File Object.
txt = open(file_name)

print "You are reading from %s file." % file_name

# Calling method to read entire file at once
print txt.read()

print "\nType the file name again:"
file_again = raw_input("> ")

# Another file object
txt_again = open(file_again)

print txt_again.read()
