# Develop small Cart application
Cart = {}
while True:
    print("1.Add product")
    print("2.Delect product")
    print("3.Update product")
    print("4.viwe Cart items ")
    print("5.Exit")
    opt = input("Enter your Option: ")

#Adding the Product in the Cart...
    if opt == "1":
        Product=input("Enter the Product Name: ")
        if Product in Cart:
            print("*"*40)
            print(f" {Product} is Exit in the Cart..")
            print("*"*40)
        else:
            Qut =int(input(f"Enter the quality of {Product}:"))
            Cart [Product] = Qut
            print("*"*40)
            print (f" {Product}->{Qut} adding the Cart..")
            print("*"*40)
        
#Remove ing the Product in the cort...
    elif opt =="2":
        Product = input("Enter the Product Name:")
        if Product in Cart:
            del Cart[Product]
            print("*"*40)
            print (f" {Product} Was Delected down..")
            print("*"*40)
        else:
            print("Product not They in The Cart..")
        
#Updateing the product quality if the product in the Cart...
    elif opt == "3":
        Product = input("Enter the Product Name: ")
        if Product in Cart:
            Qut =int(input(f"Enter the {Product} New Quality: "))
            Cart [Product]=Qut
            print("*"*40)
            print(f"{Product}-->{Qut} Was Updateing Down..")
            print("*"*40)
        else:
            print("*"*40)
            print (f"{Product} Not in the Cart...")
            print("."*40)
#viwe the Product in the cart...

    elif opt == "4":
        if Product in Cart:
            for Product, Qut in Cart.items():
                print("*"*40)
                print(f"{Product} -->{Qut}")
                print("*"*40)
        else:
            print("*"*40)
            print("No itmes in the cart...")
            print("*"*40)

#Exit the Product in the Cart...

    elif opt =="5":
        a = input("Are you Sure Exit in the Cart (yes/no) : ")
        if a == "yes":
            print("*"*40)
            print("Thank you....")
            print("*"*40)
            break
        else:
            print("you have continue the shopping")
        
#Check option valid or invalid....
    else:
        print(f"{opt} Invalide option Try Again: ")