import sys

numbers = list(sys.argv[1:])
numbers = sorted(numbers)
final = False
for i, number in enumerate(numbers[:-1]):
    if number == numbers[i + 1]:
        final = True
        break
print final
