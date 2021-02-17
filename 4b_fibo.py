import sys
import decimal
with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
    inputValue = int(lines[0])

if inputValue <= 1:
    print(inputValue)
    exit(0)
f0 = decimal.Decimal(0)
f1 = decimal.Decimal(1)
f2 = decimal.Decimal(0)
for n in range(1, inputValue):
    f2 = f0 + f1
    f0 = f1
    f1 = f2
print(f2)