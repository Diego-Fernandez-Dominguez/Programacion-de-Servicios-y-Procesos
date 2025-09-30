def exercise10(num1:int, num2:int):
    if num1 > num2:
        print(num1)
    elif num2 > num1:
        print(num2)
    else:
        print("They're equals")

def main():
    num1=int(input("say A number: "))

    num2=int(input("say ANother number: "))

    exercise10(num1,num2)

if __name__ == "__main__":
    main()
