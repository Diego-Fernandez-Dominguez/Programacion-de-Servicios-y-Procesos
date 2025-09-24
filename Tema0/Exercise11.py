def exercise11(vocal1:chr):

    lista = ["a", "e", "i", "o", "u"]

    return lista.__contains__(vocal1)


def main():
    vocal=input("sAY IT")

    result=exercise11(vocal)

    if result:
        print("Good boy")
    else:
        print("Bad boy")

if __name__ == "__main__":
    main()
