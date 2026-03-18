# simple loops
for i in range(5):
    print(i)

for i in range(1,11):
    print(i)

for i in range(1,20,2):
    print(i)

arr = [2,3,4,5,6]

total = 0
for num in arr:
    total+= num

print(total)

arr = [2,3,4,5,6]

for num in arr:
    if num%2 == 0:
        print(num)
    else:
        break

i=0
while(i>5):
    print(i)
    i+=1