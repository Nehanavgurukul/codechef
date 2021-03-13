price1 = int(input("enter the price"))
price2 = int(input("enter the price"))
price3 = int(input("enter the price"))

if(price1 >= price2):
    if(price1 >= price3):
        print(price1, "is max")
elif(price2 >= price1):
    if(price2 >= price3):
        print(price2, "is max")
elif(price3 >= price1):
    if(price3 >= price2):
        print(price3, "is max")
        