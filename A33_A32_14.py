num1 = int(input("enter the number"))
num2 = int(input("enter the number"))
i = 1
while(True):
    if(i%num1 == 0 and i%num2 == 0):
        print("LCM is",i)
        break
    i = i + 1
