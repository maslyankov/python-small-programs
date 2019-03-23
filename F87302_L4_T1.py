import sys

d = {1: 'a', 2: 'b', 3: 'c', 4: 'a', 5: 'd', 6: 'e', 7: 'a', 8: 'b'}
values = {}
key = sys.argv[1:];

for k in d:
    values.setdefault(d[k], [])
    values[d[k]].append(k)

print values.get(key[0], [])
