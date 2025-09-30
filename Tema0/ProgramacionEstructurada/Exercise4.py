import random

randomNumber=random.randint(1, 101)

print(random)

number=int(input("Say a number matao: "))

while number!=randomNumber and number!=-1:

    if randomNumber>number:
        print("Higher")
    elif number>randomNumber:
        print("Lower")
    
    number=int(input("Tell me another number: "))

print("CONTGRATULATIONS, you are acertado, felicitations")