import sys

numbers = sys.argv[:]

numbers = sorted(numbers)
out = []
for i, number in enumerate(numbers[:-1]):
    if number != numbers[i - 1]:
        out.append(number)

print(out)
