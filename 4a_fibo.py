import sys
import decimal
with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
    inputValue = float(lines[0])

def fibo(n):
    if n <= 1:
        return decimal.Decimal(n)
    return fibo(n - 2) + fibo(n - 1)

print(fibo(inputValue))