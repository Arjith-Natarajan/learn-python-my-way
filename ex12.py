# Getting Input with Prompts Directly

# Re-Writing ex11.py with Prompts
age =  raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = int(raw_input("How much do you weigh?"))

print "You are %r yrs old, %r tall and %d heavy. " % (
        age, height, weight)
