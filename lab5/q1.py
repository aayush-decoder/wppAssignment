from math import *

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
maxXor = 0

for i in range(a, b+1):
    for j in range(a, b+1):
        if i^j > maxXor:
            maxXor = i^j
        elif i^j == 2 ** max(i, j).bit_length() -1:
            maxXor = i^j 
            break

print(maxXor)
