x=10
# Missing colon
if x > 5  # SyntaxError
    print("Big number")

# Corrected code
if x > 5:   
    print("Big number")

# Division by zero
result = 10 / 0  # ZeroDivisionError

# Variable doesn't exist
print(score)  # NameError

# Wrong type
print(type("hello" + 5))  # TypeError

# For handling errors



#ex 1:
try:
    # Code that may raise an error
    result = 10 / 0 
except ZeroDivisionError:
    print("Cannot divide by zero!")

#ex 2:

try:
    age = int(input("Enter your age: "))
    print(f"In 10 years, you'll be {age + 10}")
except ValueError:
    print("Please enter a number")

#ex 3:
try:
    # Read a number from a file
    with open('number.txt', 'r') as f:
        text = f.read()
    number = int(text)
    result = 100 / number
    print(f"Result: {result}")
except FileNotFoundError:
    print("Could not find number.txt")
except ValueError:
    print("File doesn't contain a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

#ex 4:
try:
    with open('data.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
else:
    # This only runs if the file was opened successfully
    print(f"File has {len(data)} characters")

#ex 5:
try:
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    # This always runs to clean up
    if 'file' in locals() and not file.closed:
        file.close()
    print("Cleanup complete")


# another error


#ex 1:

# This fails if file doesn't exist
with open('missing.txt', 'r') as f:
    content = f.read()

#ex 2:

import os

# Check first
if os.path.exists('data.txt'):
    with open('data.txt', 'r') as f:
        content = f.read()
else:
    print("File not found")

# Or use try-except
try:
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    content = ""  # Default value

#ex 3:

# These cause ValueError
int("hello")        # Can't convert to number
int("12.5")         # int() doesn't accept decimals
list.remove("x")    # Item not in list

# Validate user input(solution):
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a number")

# Convert carefully
float_str = "12.5"
number = int(float(float_str))  # Convert to float first

#ex 4:

user = {"name": "Alice", "age": 25}
print(user["email"])  # KeyError - no email key

#solution:
# Check if key exists
if "email" in user:
    print(user["email"])

# Use get() with default
email = user.get("email", "no-email@example.com")

# Or handle the error
try:
    print(user["email"])
except KeyError:
    print("Email not found")

#ex 5:

numbers = [1, 2, 3]
print(numbers[5])  # IndexError - only 3 items

#solution:
# Check length first
if len(numbers) > 5:
    print(numbers[5])

# Use negative indexing carefully
last_item = numbers[-1] if numbers else None

# Handle the error
try:
    print(numbers[5])
except IndexError:
    print("List too short")

#ex 6:

# These cause TypeError
"hello" + 5            # Can't add string and number
len(42)                # Numbers don't have length
int([1, 2, 3])         # Can't convert list to int

#solution:
# Convert types explicitly
value = "hello" + str(5)       # "hello5"
value = str(42)                # "42"

# Check type first
if isinstance(value, str):
    print(len(value))

#ex 7:

text = "hello"
text.append("!")  # AttributeError - strings don't have append

#solution:

# Use correct methods
text = "hello"
text = text + "!"  # Strings are immutable

# Check if attribute exists
if hasattr(text, 'append'):
    text.append("!")
else:
    print("Strings don't have append method")

