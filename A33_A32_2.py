# this code for 49, 3, 1024
# n = int(input("enter the number"))
# low = 1
# high = n+1
# c = 1
# while(c<=10):
#     m = (low+high)/2
#     c = c + 1
#     if(m*m > n):
#         high = m
#     elif(m*m == n):
#         print(m)
#     else:
#         low = n 
# print(m)


# this code for 1024, 210, 1
n = int(input("enter the number"))
res = 1
p = 2
while(p<=n):
    c = 0
    if(n%p == 0):
       c = c + 1
       n = n // p
    else:
        res = res *(c+1)
        p = p +1
print(res)