import sys

a = 0.0
n = 0
with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
    a = float(lines[0])
    n = int(lines[1])
p = 1.0
for current in range(0, n):
    p = p * a
print(p)