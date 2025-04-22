def isPanagram(sentence):
    sentence = sentence.lower()
    lst = []
    for letter in sentence:
        if letter not in lst and 97 <= ord(letter) <= ord('z'):
            lst.append(letter)
    
    return "panagram" if len(lst) == 26 else "not panagram"

sentence = input("Enter the word: ")
print(isPanagram(sentence)) 