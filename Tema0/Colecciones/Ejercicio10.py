encryption = {'e':'p','i':'v','k':'i','m':'u','p':'m','q':'t','r':'e','s':'r','t':'k','u':'q','v':'s'}

counter=0

text=input("Tell me a joke: ")

text2=""

for letter in text:
   
    if letter in encryption:
        text2+=encryption[letter]
        
    else:
        text2+=letter

print(text2)