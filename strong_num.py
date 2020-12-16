num=int(input("inter the number "))
num1=num
sum=0
while(0<num):
    a=num%10
    num=num//10
    multi=1
    while(0<a):
        multi=multi*a
        a=a-1
    sum=sum+multi
if(num1==sum):
    print("yes strong number")
else:
    print("not strong number")