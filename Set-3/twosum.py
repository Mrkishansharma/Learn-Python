a=[2, 7, 11, 15,6,4]
t = 9

a.sort()

i=0
j=len(a)-1

while i<j:
    sum=a[i]+a[j]
    if(sum==t):
        print(i,j)
        break
    elif(sum>t):
        j-=1
    else:
        i+=1
