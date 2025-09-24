
userNumber=int(input("Enter number: "))

for counter in range(1,userNumber+1):

    print(" " * int(userNumber-counter), end="")
    print("* ", end="")

    if(counter>1):
        print("* " * int(counter-1), end="")

    print("")