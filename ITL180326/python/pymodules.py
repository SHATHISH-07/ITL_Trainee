import math
import random
from datetime import datetime
import os 

print(math.sqrt(4))
print(math.floor(math.pi)) # Rounds to the smallest possible
print(math.ceil(math.pi)) # Rounds the decimal to it largest possible

# Random Values

print(random.randint(1,10))
print(random.choice([1,2,3,4,5]))

# Date time

now = datetime.now()
print(now)

# os module
print(os.curdir)