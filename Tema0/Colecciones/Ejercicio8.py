productList={}

value=0

while value != 4:

    print("1.Add product - 2.Sold - 3.Print - 4.Exit")
    value=int(input("Choose an option: "))


    match value:
        case 1:
            name=input("Write the name of the product: ")

            if name in productList:
                print("The product alredy exists")
            else:
                productList[name]=0
                    
        case 2: 
            name=input("Write the name of the product: ")

            if name not in productList:
                print("The product doesn't exists")
            else:
                number=int(input("How many products have been sold: "))
                if number <= 0:
                    print("The number must be higher than 0")
                else:
                    productList[name]+=number
        
        case 3:
            print(productList)
        
        case 4:
            print("PROGRAM TERMINATED")

