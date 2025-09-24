def exercise9(num1:int, num2:int):
    for counter in range (num1+1, num2):
        print(counter)

def main():
    num1=int(input("say A number: "))

    num2=int(input("say ANother number: "))

    exercise9(num1,num2)

if __name__ == "__main__":
    main()
