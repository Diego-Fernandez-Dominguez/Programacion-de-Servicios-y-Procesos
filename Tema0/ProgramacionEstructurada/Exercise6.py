userNumber=int(input("Say a number: "))

factorial=1

for counter in range(1,userNumber+1):
    factorial*=counter

print(factorial)