
file = open("example.txt", "r") 

content = file.read()          

file.close()            

c=0

for ch in content:
    if(ch==' '):
        c+=1

print(c+1)


file = open("output.txt", "w")  

file.write('Number of words is : '+ str(c+1))   

file.close()                    

