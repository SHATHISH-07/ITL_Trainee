import json
import requests
import csv

# opening a file and reading the file
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Opening a file for writing
file1 = open("data.txt", "w")
content = file1.write("I am replacing the old message with this")
file1.close()

# Opening a existing file to append new content to it
file = open("data.txt","a")
content = file.write("\n This is the new line i have appended to the existing data.txt file")
file.close()

# opening a fie to read and append a new content to it
file = open("data.txt","a+")
file.write("\nThis is the fifth line")
file.write("\nThis is the sixth line")
file.seek(0)
for line in file:
    print(line)
file.close()

# using auto close with to open a file for reading and writing
with open("data.txt", "r+") as file:
    content = file.read()
    file.seek(0)
    file.write("Updated Content")

# opening a file for reading and changing a particular line and writing the entire line to the file by replacing the old content
with open("data.txt","r") as file:
    lines = file.readlines()
lines[4] = "This the Update line \n"
with open("data.txt","w") as file:
    file.writelines(lines)

# creating a new called NewFile.txt and reading
with open("NewFile.txt","x+") as file:
    file.write("This is a new file created")
    file.seek(0)
    print(file.read())

#json implementation

# opening a json file for reading
with open("demo.json","r") as f:
    data = json.load(f)
    print(data["name"])

# opening a json file for appending a new content and reading
with open("demo.json","a+") as f:
    data = {
        "name":"shathish Kumaran",
        "native":"Chennai"
    }
    json.dump(data,f,indent=4)


# using loads and dumbs for string to dict and dict to string conversion
data = {"name": "Shathish"}
s = json.dumps(data)
d = json.loads(s)
print(s)
print(d)

# using external api to fetch json data and storing it to the file called demo.json
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()
with open("demo.json","w") as f:
    json.dump(data,f,indent=4)
print(data)

# reading the demo.json file adnd filtering the user and dump the filtered user in new file
with open("demo.json","r") as f:
    data = json.load(f)
filteredUser = []
for user in data:
    if "Group" in user["company"]["name"]:
        filteredUser.append(user)
with open("filteredUser.json","w") as f:
    json.dump(filteredUser,f,indent=4)

#csv implementation

# opening a csv file for reading
with open("demo.csv","r") as f:
    reader = csv.reader(f)
    next(reader) # leaves the header
    for row in reader:
        print(row)

# opening a csv file for writing
with open("demo.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name","age","city"])
    writer.writerow(["santhoush","41","Patty"])

# opening a new csv file to write dictionary value to csv into a csv file
with open("demo.csv","w") as f:
    fieldNames = ["name","age","city"]
    writer = csv.DictWriter(f,fieldnames=fieldNames)
    writer.writeheader()
    writer.writerow({"name":"shathish","age":21,"city":"Salem"})

# reading a csv in dictionary format
with open("demo.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"],row["city"])

# reading the json data and mapping and storing in a variable
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

# writing the json data into the csv file as a csv format
with open("demo.csv","w",newline="") as f:
    filedNames = ["name","username"]
    writer = csv.DictWriter(f,fieldnames=filedNames)

    writer.writeheader()

    writer.writerows(csvData)