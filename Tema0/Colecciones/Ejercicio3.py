list = []
counter=0
number=0
var1=""

while len(list) < 8:
    list.append(int(input("Tell me a number, son of your mother: ")))

while counter<len(list):
    number=list[counter]
    counter=counter+1
    var1= "pair" if (number%2 ==0) else "impair"
    print(var1)