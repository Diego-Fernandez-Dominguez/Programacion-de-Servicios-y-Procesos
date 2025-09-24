def suma(num1, num2):
    return(num1+num2)

def resta(num1, num2):
    return(num1+num2)

def multiplicacion(num1, num2):
    return(num1+num2)

def division(num1, num2):
    return(num1+num2)

num1=int(input("Say a number: "))
num2=int(input("Say another number: "))


print("Choose an option: 1.Suma - 2.Resta - 3.Multiplicacion - 4.Division")
value=int(input("Say an option: "))


match value:
    case 1:
        print(suma(num1,num2))
    case 2:
        print(resta(num1,num2))

    case 3:
       print(multiplicacion(num1,num2))

    case 4:
        print(division(num1,num2))
