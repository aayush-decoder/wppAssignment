l = int(input("Enter the length in feet: "))

instructions = "Menu:\n1.Convert to inches\n2.Convert to yards\n3.Convert to miles\n4.Convert to millimeters\n5.Convert to centimeters\nEnter 0 to exit\n"
command = True
lst=[]
print(instructions)

lst.append(l*12)
lst.append(l/3)
lst.append(l/5280)
lst.append(l*304.8)
lst.append(l*20.48)

while command:
    command = int(input("Choose an option: "))
    
    try:
        if command != 0:
            print(lst[command-1])
    except:
        pass