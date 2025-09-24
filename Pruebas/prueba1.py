print("Hola mundillo")
user_name=input("Dime tu nombre matao: ")
print("Wenas tardes " + user_name)
age=int(input("Ahora dime tu edad que le sumo uno, soy un genio chavalin: "))
age=age+1
print("Mañana tienes " + str(age) + " años, si mañana, si lo digo yo es así")

triple= """vaya locura
de linea loco"""

print(triple)

#vaya comentario loquete
 
first_text="Hello champ"
second_text="You're the goat"

third_text=first_text + ", " + second_text
print(third_text)

third_text=second_text*3
print(third_text)

print("Lenght= " + str((len(third_text))))

print(8**2) # Elevado
print(14//3) # Division entera
print(8%3) # Modulo

print(first_text[0]) # H
print(first_text[1:7]) # ello c

words=second_text.split(" ")
print(words)
words2=" ".join(words)
print(words2)

if age<18:
    print("You`re a minor, go truck yourself")
elif age >=18 and age < 30:
    print("You`re an adult, go to work and do something")
else:
    print("You`re semideath, do the testament")

var1= "pair" if (age%2 ==0) else "impair" # IF en una sola linea
print(var1)

number=0

while number < 5:
    number=number+1
    print(str(number))

for letter in second_text:
    print(letter)

for counter in range(1,6):
    print(counter)

def function_1(param1, param2):
    res=param1+param2
    return res

result=function_1(1, 2)
print("YEIIII " + str(result))

def salute(name="Joselin"):
    print("Hello " + name)

salute("me")
salute()

cadena="teheechadodemenostodoestetiempo" 

lista = [1, 2, 3, 4, 5]

for letra in cadena:
    print(letra)

for contador in range(1, 10, 2):
    print(contador)

for valor in lista:
    print(valor)