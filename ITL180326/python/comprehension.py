arr = [1,2,3,4,5]

# list comprehension
sqrd_arr = [x**2 for x in arr]
print(sqrd_arr)

even_arr = [x for x in arr if x%2==0]
print(even_arr)

result = ["even" if x%2==0 else "odd" for x in arr]
print(result)

# dictionary comprehension
sqrd_dict = {x: x**2 for x in arr}
print(sqrd_dict)

odd_arr = {x: "odd" if x%2!=0 else "even" for x in arr}
print(odd_arr)

# set comprehension
arr1 = [1,1,2,3,4,4,5]

unique_squrd = {x**2 for x in arr}
print(unique_squrd)