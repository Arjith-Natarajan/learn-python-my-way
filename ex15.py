# Importing necessary modules from packages

from sys import argv

script, file_name = argv

 # Creating File Object.
txt = open(file_name)

print "You are reading from %s file." % file_name

# Calling method to read entire file at once
print txt.read()

# Closing the file object
txt.close()

print "\nType the file name again:"
file_again = raw_input("> ")

# Another file object
txt_again = open(file_again)

# Printing the contents on the console
# Using readline method instead of read
print txt_again.readline()

# readlines returns a list of string
# from current position of file ptr
print txt_again.readlines()
txt_again.close()
