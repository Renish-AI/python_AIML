# Pattern 1: Import the whole module
import math
math.sqrt(16)

# Pattern 2: Import specific items from a module
from math import sqrt, pi
sqrt(16)

# Import entire module
import random

# Use module functions
number = random.randint(1, 10)
print(f"Random number between 1 and 10: {number}")
choice = random.choice(["apple", "banana", "orange"])

# Date and time
import datetime
today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)

# Import entire module
import math
result = math.sqrt(16)

# Import specific functions
from math import sqrt, pi
result = sqrt(16)
circle_area = pi * 10 ** 2

# Import with alias
import pandas as pd
df = pd.DataFrame(data)

# Import everything (avoid this!)
from math import *

import numpy as np
array = np.array([1, 2, 3, 4, 5])
mean = np.mean(array)
print(f"Mean: {mean}")

import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()