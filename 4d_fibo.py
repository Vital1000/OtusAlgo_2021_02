import sys
import decimal

with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
    inputValue = int(lines[0])

if inputValue <= 1:
    print(inputValue)
    exit(0)

baseM = [[1, 1], [1, 0]]
def mulMatrix2x2(m1, m2):
    # m1[0][0] m1[0][1]   m2[0][0] m2[0][1]
    # m1[1][0] m1[1][1]   m2[1][0] m2[1][1]
    m3_0_0 = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
    m3_0_1 = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
    m3_1_0 = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
    m3_1_1 = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
    m3 = [[m3_0_0, m3_0_1], [m3_1_0, m3_1_1]]
    return m3

current = inputValue - 1
currentPow = baseM
result = [[1, 0], [0, 1]]
while current >= 1:
    if current % 2 == 1:
       result = mulMatrix2x2(result, currentPow)
    current = int(current / 2)
    currentPow = mulMatrix2x2(currentPow, currentPow)

print(result[0][0])