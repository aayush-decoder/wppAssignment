def numOfOperations(word):
    def corres(num):
        index = len(word)-num-1
        if index<0:
            index += index
        return index
    count = 0
    # markedIndex = len(word)/2 if len(word)%2==0 else (len(word)+1)/2
    for i in range(len(word)//2):
        if ord(word[i]) != ord(word[corres(i)]):
            count += abs( ord(word[i]) - ord(word[corres(i)]) )
    return count

n = int(input("Enter the number of inputs: "))
for i in range(n):
    new_word = input("New word: ")
    print("Number of operations needed: ", numOfOperations(new_word)) 

