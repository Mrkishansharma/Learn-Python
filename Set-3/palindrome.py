st='naman'

i=0
j=len(st)-1
flag=1
while i<j:
    if(st[i]!=st[j]):
        flag=0
        break
    else:
        i+=1
        j-=1

if(flag):
    print('Palindrome')
else:
    print('Not Palindrome')