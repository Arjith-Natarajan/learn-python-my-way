# importing necessary modules
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_data = open(from_file).read()

print "The input file is %d bytes long." % len(in_data)

print "Does the output file really exists?  %r" % exists(to_file)
print "Ready , hit RETURN to continue, CTRL-C to abort"
raw_input()

open(to_file,'w').write(in_data)

print "Wrapping up and closing"
