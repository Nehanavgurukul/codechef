a=int(input("enter the number"))  # LCM question 
b=int(input("enter the number"))
i=2
while(a>0):
    if (i%b==0 and i%a==0):
        print(i)
        break
    i=i+1
