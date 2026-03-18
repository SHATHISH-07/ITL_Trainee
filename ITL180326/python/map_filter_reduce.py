from functools import reduce

arr = [1,2,3,4,5]

# using map function
array_square = list(map(lambda x: x*x, arr))
print(array_square)

# using filter function
array_even = list(filter(lambda x: x%2==0, arr))
print(array_even)

# using reduce function from the functools package
array_sum = reduce(lambda x, y: x + y, arr)
print(array_sum)