def addFunc(num):
    if num<10:
        return num
    num = str(num)
    sum=0
    for i in num:
        sum += int(i)
    return addFunc(sum)

number= int(input("Enter a number: "))
print("The digital root is: ", addFunc(number))