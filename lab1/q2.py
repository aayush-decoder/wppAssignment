import random

lst = [random.randint(0, 1) for x in range(0, 100)]

count = 0
max = 0

for i in lst:
    if i==1:
        max = count if max < count else max
        count = 0
    elif i==0:
        count += 1
    else:
        count = 0

print(lst)
print("\ncount: ", max)