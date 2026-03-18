# Simple function for greet and square a number
def greet(msg):
    print(msg)

greet("hello")

def square_no(x):
    print("The square of the number is:", x*x)

square_no(2)

# using advanced lambda function for squaring a number
lambda_square = lambda x: x*x

print("Squared a number using lambda function",lambda_square(2))

# Function with default value
def greetDefault(name="User"):
    print(f"hello {name}")

greetDefault()
greetDefault(name="Shathish")

# function with value passed using key
def greet(first, last):
    print(f"hello {first} {last}")

greet(last="Kumaran", first="Shathish")

# using args to pass multiple values
def sum_num(*args):
    print(sum(args))

sum_num(1,2,3,4,5)

# using key value args to pass values
def user_info(**kwargs):
    return kwargs

user_data = user_info(name="Shatihsh",role="Trainee")
print(user_data)