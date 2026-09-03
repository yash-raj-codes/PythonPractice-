# ==========================================
# 1. VARIABLES, DATA TYPES, & PRINTING
# ==========================================
# Variables store data. Python automatically detects the data type.

name = "Yash"           # String (text)
age = 19                # Integer (whole number)
height = 5.9            # Float (decimal number)
is_student = True       # Boolean (True or False)

# Printing with F-strings (formatted strings)
print("--- 1. Variables & Outputs ---")
print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}\n")


# ==========================================
# 2. OPERATORS (Arithmetic & Comparison)
# ==========================================
# Operators perform mathematical or logical actions.

print("--- 2. Operators ---")
sum_val = 10 + 5        # Addition (15)
power = 2 ** 3          # Exponent/Power (2 to the power of 3 = 8)
remainder = 10 % 3      # Modulo (remainder of 10/3 = 1)
is_greater = 10 > 5     # Comparison (True)

print(f"10 + 5 = {sum_val}")
print(f"2^3 = {power}")
print(f"Remainder of 10/3 = {remainder}")
print(f"Is 10 > 5?: {is_greater}\n")


# ==========================================
# 3. CONDITIONAL STATEMENTS (if-elif-else)
# ==========================================
# Controls the flow of code based on conditions.

print("--- 3. Conditionals ---")
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # This will run because 85 is >= 80
else:
    print("Grade: C")
print("")


# ==========================================
# 4. LOOPS (For & While)
# ==========================================
# Loops repeat a block of code multiple times.

print("--- 4. Loops ---")
# For loop: Runs a specific number of times (range(3) means 0, 1, 2)
print("For Loop output:")
for i in range(3):
    print(f"  Loop iteration: {i}")

# While loop: Runs as long as a condition is true
print("While Loop output:")
counter = 3
while counter > 0:
    print(f"  Countdown: {counter}")
    counter -= 1  # Decrement counter by 1
print("")


# ==========================================
# 5. DATA STRUCTURES (Lists, Tuples, Dicts)
# ==========================================
# These structures hold collections of data.

print("--- 5. Data Structures ---")

# List: Ordered, changeable collection
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add item
print(f"List (Changed): {fruits}")
print(f"First item: {fruits[0]}")  # Indexing starts at 0

# Tuple: Ordered, unchangeable collection
coordinates = (10, 20)
print(f"Tuple (Fixed): {coordinates}")

# Dictionary: Key-value pairs
user = {
    "username": "coder123",
    "role": "admin"
}
print(f"Dictionary Role: {user['role']}\n")


# ==========================================
# 6. FUNCTIONS
# ==========================================
# Functions are reusable blocks of code. They accept parameters and return values.

print("--- 6. Functions ---")

def greet_user(username):
    """This function greets the user."""
    return f"Hello, {username}! Welcome back."

# Calling the function and saving the output
greeting_message = greet_user("Bob")
print(greeting_message)
print("")


# ==========================================
# 7. ERROR HANDLING (try-except)
# ==========================================
# Prevents the program from crashing when an error happens.

print("--- 7. Error Handling ---")
try:
    # Trying to divide by zero (which is impossible)
    result = 10 / 0
except ZeroDivisionError:
    # Code runs this block if a ZeroDivisionError happens
    print("Error: You cannot divide a number by zero!")
finally:
    # This block always runs, no matter what
    print("Execution of error block completed.\n")


# ==========================================
# 8. FILE HANDLING (Writing & Reading)
# ==========================================
# Code to save data to a file and read it back.

print("--- 8. File Handling ---")
filename = "sample.txt"

# 'w' mode creates or overwrites a file
with open(filename, "w") as file:
    file.write("Python is awesome!\nLearning is fun.")
print("Saved text to 'sample.txt'.")

# 'r' mode reads a file
with open(filename, "r") as file:
    content = file.read()
    print("Reading from file:")
    print(content)
