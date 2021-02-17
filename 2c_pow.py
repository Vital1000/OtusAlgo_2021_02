import sys

with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
    a = float(lines[0])
    n = int(lines[1])
current = n
p = 1.0
apow = a
while current >= 1:
    if current % 2 == 1:
        p = p * apow
    current = int(current / 2)
    apow = apow * apow
print(p)