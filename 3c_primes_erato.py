import sys

with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
    inputValue = int(lines[0])

numbers = []
startNumber = 0
last = inputValue + 1
for n in range(startNumber, last):
    numbers.append(n)

current = 2
while current <= inputValue:
    for n in range(current + current, last, current):
        numbers[n] = 0
    current += 1
    while current <= inputValue and numbers[current] == 0:
        current += 1

count = 0
for n in range(startNumber + 2, last):
    if numbers[n] != 0:
        count += 1

print(count)