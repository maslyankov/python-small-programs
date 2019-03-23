import sys

plain = sys.argv[1]

key = int(sys.argv[2])
translated = ''

for i in plain:
    if i.isalpha():
        num = ord(i)
        num += key

        if i.isupper():
            if num > ord('Z'):
                num -= 26
            elif num < ord('A'):
                num += 26
        elif i.islower():
            if num > ord('z'):
                num -= 26
        elif num < ord('a'):
            num += 26

        translated += chr(num)
    else:
        translated += i

print translated
