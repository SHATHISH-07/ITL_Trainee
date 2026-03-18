# a = 10
# b=0

# try:
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print("Number cannot be divided by zero")

try:
    file = open("data.txt","r")
    try:
        data = file.read()
        print('file opened and readed...')
        print(data)
    except Exception as e:
        print("Not able to read the file:", e)
except FileNotFoundError:
    print("Ensure the file is exist...")
    print("File Not Found Error...")
finally:
    try:
        file.close()
        print("file closed...")
    except:
        print("No file to close...")
    