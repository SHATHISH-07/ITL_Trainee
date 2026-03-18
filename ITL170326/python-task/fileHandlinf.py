import json
import requests
import csv

# file = open("data.txt", "r")

# content = file.read()

# print(content)

# file.close()


# file1 = open("data.txt", "w")

# content = file1.write("I am replacing the old message with this")

# file1.close()


# file = open("data.txt","a")

# content = file.write("\n This is the new line i have appended to the existing data.txt file")

# file.close()


# file = open("data.txt","a+")

# file.write("\nThis is the fifth line")
# file.write("\nThis is the sixth line")

# file.seek(0)

# for line in file:
#     print(line)

# file.close()

# with open("data.txt", "r+") as file:
#     content = file.read()

#     file.seek(0)
#     file.write("Updated Content")

# with open("data.txt","r") as file:
#     lines = file.readlines()

# lines[4] = "This the Update line \n"

# with open("data.txt","w") as file:
#     file.writelines(lines)


# with open("NewFile.txt","x+") as file:
#     file.write("This is a new file created")

#     file.seek(0)

#     print(file.read())


# with open("demo.json","r") as f:
#     data = json.load(f)
#     print(data["name"])


# with open("demo.json","a+") as f:
#     data = {
#         "name":"shathish Kumaran",
#         "native":"Chennai"
#     }
#     json.dump(data,f,indent=4)

# data = {"name": "Shathish"}

# s = json.dumps(data)

# d = json.loads(s)

# print(s)
# print(d)

# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)

# data = response.json()

# with open("demo.json","w") as f:
#     json.dump(data,f,indent=4)

# print(data)


# with open("demo.json","r") as f:
#     data = json.load(f)

# filteredUser = []

# for user in data:
#     if "Group" in user["company"]["name"]:
#         filteredUser.append(user)

# with open("filteredUser.json","w") as f:
#     json.dump(filteredUser,f,indent=4)

# with open("demo.csv","r") as f:
#     reader = csv.reader(f)

#     next(reader)

#     for row in reader:
#         print(row)


# with open("demo.csv","w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["name","age","city"])
#     writer.writerow(["santhoush","41","Patty"])


# with open("demo.csv","w") as f:
#     fieldNames = ["name","age","city"]
#     writer = csv.DictWriter(f,fieldnames=fieldNames)

#     writer.writeheader()
#     writer.writerow({"name":"shathish","age":21,"city":"Salem"})


# with open("demo.csv","r") as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         print(row["name"],row["city"])

with open("filteredUser.json","r") as f:
    data = json.load(f)

    csvData = []
    for d in data:
        csvData.append(
            {
                "name":d["name"],
                "username":d["username"]
            }
        )

with open("demo.csv","w",newline="") as f:
    filedNames = ["name","username"]
    writer = csv.DictWriter(f,fieldnames=filedNames)

    writer.writeheader()

    writer.writerows(csvData)