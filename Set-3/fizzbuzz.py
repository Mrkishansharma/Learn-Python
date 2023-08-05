
a=[]

for i in range(1,101):
    a.append(i)


for i in a:
    if(i%3==0 and i%5==0):
        print('Fizz Buzz')
    elif(i%3==0):
        print('Fizz')
    elif(i%5==0):
        print('Buzz')
    else:
        print(i)