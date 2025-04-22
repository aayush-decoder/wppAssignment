def takeInput():
    num = input("Enter a number: ")
    count=0
    for n in num:
        if int(num)%int(n)==0:
            count += 1
    return count

length = int(input("Enter the number of words: "))
lst=[]
for i in range(length):
    lst.append(takeInput())

for item in lst:
    print(item)