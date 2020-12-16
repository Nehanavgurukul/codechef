n=4
i=0           #  favonency serice 
a=0
b=1
sum=0
while(i<n):
    sum=b+a
    b=a
    a=sum
    i=i+1
print(sum)