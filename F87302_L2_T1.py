# Check if a list is sorted or not.

import sys

numbers = list(sys.argv[1:])
isSorted = 1
for i, n in enumerate(numbers[:-1]):
    if n > numbers[i + 1]:
        isSorted = 0
        break
print("sorted" if isSorted else "not sorted")
