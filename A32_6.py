num = int(input("enter the number"))

if(num > 200):
    if(num%2 == 0):
        print("Bingo")
    else:
        print("CodeChe")
elif(num < 200):
    if(num%2 != 0):
        print("Ringo")
    else:
        print("CodeChe")


