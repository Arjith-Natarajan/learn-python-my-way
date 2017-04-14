#Exercise 8 Printing and more Printing

# Declare variable which prints 4 raw data
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4) # print integers
print formatter % ("one", "two", "three", "four") # print strings
print formatter % (True, False, False, True) # print boolean
#print same variable
print formatter % (formatter, formatter, formatter, formatter)
# here the same variable is treated as a string
# print some more longer strings
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didnt sing.",
    "So I said goodnight."
)
