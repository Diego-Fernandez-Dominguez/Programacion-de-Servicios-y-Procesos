contactList={}

value=0

while value != 5:

    print("1.Add - 2.Remove - 3.Search - 4.Show list - 5.Exit")
    value=int(input("Choose an option: "))


    match value:
        case 1:
            name=input("Write the name of the contact: ")

            if name in contactList:
                print("That contact alredy exists")
            else:
                contactList[name]=int(input("Write the telephone number: "))

        case 2:
            name=input("Write the name of the contact: ")

            if name in contactList:
                del contactList[name]
            else:
                print("That contact doesn't exists")

        case 3:
            name=input("Write the name of the contact: ")

            if name in contactList:
                print("That contact is in the list")
            else:
                print("That contact is not in the list")
        
        case 4:
            print(contactList)

        case 5:
            print("Goodbye")
