list = [1,"Kishan",False]

# insert into list

for i in range(4,10):
    if(i%2):
        list.append(i)
    elif(i%3):
        list.append(True)
    else:
        list.append('Hello')

print(list)

# delete from listdata

list.remove('Hello')

del list[2]

removeonemore = list.pop(5)

print(removeonemore)


# copy listdata

temp = list.copy()

print('copy list', temp)


# sort the list

list2 = [3,1,5,2,4]

list2.sort()

print("sorted list : ",list2)