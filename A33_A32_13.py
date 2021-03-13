num1 = int(input("enter the number"))
num2 = int(input("enter the number"))

i = 1
a = 1
while(True):
    if(num1%i == 0 and num2%i == 0):
        a = a * i
        if(num1 == i):
            break
    else:
        if(num1 == i):
            break
    i = i + 1
print(a)
