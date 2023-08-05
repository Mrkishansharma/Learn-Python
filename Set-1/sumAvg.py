import math

data = [10,12,14,16,18,20]

sum=0

avg=0

for i in data:
    sum+=i


avg=math.floor(sum/len(data))

print(sum,avg)