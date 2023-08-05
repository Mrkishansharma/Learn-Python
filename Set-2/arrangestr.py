
st = "KisShan"

res=''

res2=''

for char in st:
    if(char.islower()):
        res+=char
    else:
        res2+=char

print(res+res2)