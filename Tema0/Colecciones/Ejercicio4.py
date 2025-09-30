list = []

while len(list) < 10:
    list.append(int(input("Tell me a number, son of your mother: ")))

print("No ordenados: ", list)

list.sort()

print("Ordenados: ",list)