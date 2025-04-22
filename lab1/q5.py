lst = []

print("Enter exit() or done to terminate\n")

while True:
    name = input("Enter the name: ")

    if name == "exit()" or name == "done":
        break

    if len(name) > 15:
        temp = name[:16]
        lst.append(temp[::-1] + name[16:])
    else:
        lst.append(name[::-1])

    

print(lst)