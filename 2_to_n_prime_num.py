n=int(input("enter the number"))
b=1
c=2
while(b<=n):
        i=2
        while(i<c):
            if(c%i==0):
                break
            i=i+1
        else:
            print(c,"is prime")
            b=b+1
        c=c+1
    