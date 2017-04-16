# Trying out git merge

# Importing modules
from sys import argv

# Having lesser than 3 args gives Value Error
# Something like NullPointerException
script, first, second, third = argv

print "You are running from ", script
print "Your first variable : ", first
print "Your second variable : ", second
print "Your third variable : ", third

fourth = int(raw_input('How many more variables ?'))

print "You have remaining ", fourth ,"variables"
