word = input("Enter a word: ").lower()
lst = list(word)
for i,j in zip(lst, enumerate(lst)):
    if j[0]%2==1:
        lst[j[0]]=i.upper()
print("".join(lst))