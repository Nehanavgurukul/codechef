n=int (input("enter num"))
l=1
high=n+1
c=1
while(c<=10):
    m=(l+high)/2
    c=c+1
    if(m*m>n):
        high=m
    else:
        if(m*m==n):
            print(m)
            break
        else:
            l=m
print(m)