def isFibo(num):
    if num ==0:
        return "isFibo"
    t1=0
    t2=1
    while t2<=num:
        if t1+t2 == num:
            return "isFibo"
        t1, t2 = t2, t1+t2
    return "isNotFibo"

n = int(input("ENter the number of inputs: "))
for i in range(n):
    newNum = int(input("new number: "))
    print(isFibo(newNum))