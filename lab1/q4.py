# import random
nums = []
flatList = []
numbers = [i for i in range(1, 10001)]
union=True

for i in range(1, 6):
    nums.append([x for x in range(1, 10001) if x%5 == i])

print(nums)
print()

for numList in nums:
    flatList.extend(numList)

for i in numbers:
    if i in numbers:
        pass
    else:
        print("Not equal")
        union=False
        break

if union is True:
    print("The union of all equivalence class is equalt o the parent class")
