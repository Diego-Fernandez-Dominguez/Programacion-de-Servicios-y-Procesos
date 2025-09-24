def exercise11(vocal1:chr):

    lista = ["a", "e", "i", "o", "u"]

    if lista.__contains__(vocal1):
        print("Good boy")
    else:
        print("Bad boy")

def main():
    vocal=input("sAY IT")

    exercise11(vocal)

if __name__ == "__main__":
    main()
