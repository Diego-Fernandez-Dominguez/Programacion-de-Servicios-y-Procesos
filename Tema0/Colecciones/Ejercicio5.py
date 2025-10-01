import random

list = []
number=0

while len(list) < 100:
    list.append(random.randint(1,100))

number=int(input("Tell me a number: "))

print("- The number: ", number, " appears ", list.count(number), " times -")
print(list)

