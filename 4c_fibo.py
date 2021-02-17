import sys
import decimal
import math
with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
    inputValue = int(lines[0])

sqrt5 = math.sqrt(5.0)
phi = (1.0 + sqrt5) / 2.0
fibo = math.floor(decimal.Decimal(phi ** inputValue / sqrt5 + 0.5))
print(fibo)
