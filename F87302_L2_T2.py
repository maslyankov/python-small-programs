import sys

args = sys.argv[:]

print len(args[0]) == len(args[1]) and sorted(args[0].lower()) == sorted(args[1].lower())
