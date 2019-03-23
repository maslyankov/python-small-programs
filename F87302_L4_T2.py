# Count occurrences of chars in a string.

import sys

string = sys.argv[1]
string = sorted(string.replace(" ", "").lower())
occurrences = {}

for i in range(len(string) - 1):
    occurrences.setdefault(string[i], 1)
    if string[i] == string[i + 1]:
        occurrences[string[i]] += 1

print occurrences.items()
