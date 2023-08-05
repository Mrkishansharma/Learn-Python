n=10

a=0
b=1
c=0

for i in range(2,n+1):
    a=b
    b=c
    c=a+b

print(c)