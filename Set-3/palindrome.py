
str='naman'

i = 0
j = len(str) - 1
flag = 1
while i < j:
    if( str[i] != str[j] ):
        flag = 0
        break
    else:
        i += 1
        j -= 1

if flag:
    print('Palindrome')
else:
    print('Not Palindrome')