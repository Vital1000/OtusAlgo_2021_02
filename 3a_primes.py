import sys

# with open(sys.argv[1], 'r') as inFile:
#     lines = inFile.readlines()
#     inputValue = int(lines[0])
inputValue = 100
def isPrime(value):
    for n in range(2, value):
        if value % n == 0:
            return False
    return True
primesCount = 1 if inputValue >= 2 else 0
for n in range(3, inputValue + 1):
    if isPrime(n):
        primesCount += 1

print(primesCount)