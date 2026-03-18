arr = [1,2,3,4,5]
str_arr = ["a","b","c","d","e"]

# list slicing
print(arr[2])
print(str_arr[4])

#reversing a list
print('Reversed arr',arr[::-1])

# loop and control flow on list
for c in str_arr:
    if c == 'c':
        print(c)
    else:
        print('No match')

# string manupulation
name = "shathish Kumaran"
print(name[0])
single_char_arr = [c for c in name if c != " "]
for c in name:
    if c == " ":
        continue
    single_char_arr.append(c)
print(single_char_arr)
splitted_name = name.split(" ")
print(splitted_name)