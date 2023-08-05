
str="kishan"

vc=0
cc=0

vlist=['a','e','i','o','u']

for char in str:
    if(char in vlist):
        vc+=1
    else:
        cc+=1

print('total vowel count : ',vc)