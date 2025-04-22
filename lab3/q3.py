def afterNcycles(n):
    currentHeight = 1
    for i in range(1, n+1):
        if i%2==1:
            currentHeight*=2
        else:
            currentHeight+=1
    return currentHeight

n = int(input("Enter the number of inputs: "))
for i in range(n):
    newHeight = int(input("new number of cycles: "))
    print(afterNcycles(newHeight))