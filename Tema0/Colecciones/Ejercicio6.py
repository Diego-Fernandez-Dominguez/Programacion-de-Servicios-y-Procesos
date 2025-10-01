text=input("Tell me something: ")

dictionary={}

wordsList = text.split()

for word in wordsList:
    if word in dictionary:
        dictionary[word]+= + 1
    else:
        dictionary[word] = 1

print(dictionary)