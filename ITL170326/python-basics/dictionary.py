# sample dictionary declaration
person = {
    "name":"shathish",
    "age":12,
    "city":"chennai"
}

print(person["name"])
print(person.get("age"))

# updating the existing value in the dictionary
person["age"] = 21

print(person["age"])

# looping the disctionary
for key, value in person.items():
    print(key, value)

# control checking in dictionary
if("name" in person):
    print(True)