# A simple exercise to learn
# printing and formatted prinitng


# Variables declaration & definitions section
x = "There are %d types of people" % 10  # formatted string
binary = "binary"  # string
do_not = "don't"  # string
y = " Those who know %s and those who %s know %s" % (
    binary, do_not, binary)  # printing formatted string
num = 'hi'

print x
print y

print "I said : %r." % x
print "I also said : '%s'" % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

# print "This is value of num %s" % num

print w + e  # '+' is concatenation operator
