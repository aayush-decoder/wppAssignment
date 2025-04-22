dict={}
print("Please type 0 or done to finish entering data.")
while True:
    product = input("\nNew Product name: ")

    if product in list(dict.keys()):
        confirm = input("This product is already registered. Do you want to update it? yes or no?: ")
        if confirm == 'yes':
            dict[product] = price;
        else:
            continue
    elif product=='exit()' or product=='done' or product=="":
        break
    
    try:
        price = int(input("Product price: "))
    except:
        print("**Invalid price**")
        continue
    dict[product] = price;
    

while True:
    query = input("\nProduct you want to seach: ")

    if query in list(dict.keys()):
        print(f'Price of {query} is {dict[query]}')
    elif query == 'exit()' or query=='done' or query=="":
        break
    else:
        print("This product does not exist in the dictionary")

print()
print(dict)
