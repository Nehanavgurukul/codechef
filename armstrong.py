n=int(input("enter the number"))  # this for Armstrong number.
num=n
i=1
sum=0
while(i<=n):
    c=n%10
    n=n//10
    s=c**3
    sum=sum+s
    i=i+1
if(sum==num):
    print("yes Armstrong number")
else:
    print("not Armstrong number")
