num1 = int(input("enter the number"))
num2 = int(input("enter the number"))
num3 = int(input("enter the number"))

if(num1 > num2):
    if(num2 < num3):
        print(num1, "sec max")
    elif(num2 > num3):
        print(num2, "sec max")
elif(num2 > num1):
    if(num1 < num3):
        print(num2 , "sec max")
    elif(num1 > num3):
        print(num1, "sec max")
elif(num3 > num1):
    if(num1 < num2):
        print(num2, "sec max")
    elif(num1 > num2):
        print(num1, "sec max")
           

# if(num1 >= num2):
#     if(num1 <= num3):
#         print(num3, "sec max")
#     else:
#         print(num2, "sec max")
# elif(num2 >= num1):
#     if(num2 <= num3):
#         print(num3 , "sec max")
#     else:
#         print(num1, "sec max")
# elif(num3 >= num1):
#     if(num3 >= num2):
#         print(num2, "sec max")
#     else:
        # print(num1, "sec max")
           