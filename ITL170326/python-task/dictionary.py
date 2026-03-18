person = {
    "name":"shathish",
    "age":12,
    "city":"chennai"
}

print(person["name"])

print(person.get("age"))

person["age"] = 21

print(person["age"])


for key, value in person.items():
    print(key, value)

if("name" in person):
    print(True)