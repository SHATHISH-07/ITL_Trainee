arr = [1,2,3,4,5,5,5,6,6]

seen = set()

duplicateArr = [] # All the duplicate values

dupValue = set() # Only shows the repeted elements

for num in arr:
    if num in seen:
        duplicateArr.append(num)
        dupValue.add(num)
    else:
        seen.add(num)

print(duplicateArr)
print(list(dupValue))

