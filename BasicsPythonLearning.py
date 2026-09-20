# ==========================================
# PYTHON BASICS LEARNING FILE
# More examples + subtopics added
# ==========================================

# ==========================================
# 1. VARIABLES, DATA TYPES, AND PRINTING
# ==========================================
# Variables store data. Python automatically detects the type.
# Subtopics:
# - Variable assignment
# - Data types
# - Type checking
# - Type conversion
# - Print formatting

print("--- 1. Variables, Data Types & Printing ---")

name = "Yash"                 # String
age = 19                      # Integer
height = 5.9                  # Float
is_student = True             # Boolean
salary = None                 # NoneType

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}")
print(f"Salary: {salary}, Type: {type(salary)}")

# Multiple assignments in one line
a, b, c = 10, 20, 30
print(f"Multi Assign: a={a}, b={b}, c={c}")

# Type conversion examples
num_str = "100"
num_int = int(num_str)
print(f"String to int: {num_str} -> {num_int} (type: {type(num_int)})")

float_num = float(age)
print(f"Integer to float: {age} -> {float_num} (type: {type(float_num)})")

bool_val = bool(0)
print(f"0 to bool: {bool_val}")

# f-strings with formatting
print(f"Formatted output: {name} is {age} years old and {height} feet tall.\n")


# ==========================================
# 2. OPERATORS
# ==========================================
# Operators are used to perform operations.
# Subtopics:
# - Arithmetic operators
# - Comparison operators
# - Assignment operators
# - Logical operators
# - Identity operators
# - Membership operators

print("--- 2. Operators ---")

# Arithmetic operators
sum_val = 10 + 5
diff = 20 - 8
product = 4 * 6
division = 20 / 3
floor_division = 20 // 3
power = 2 ** 3
remainder = 10 % 3

print(f"Addition: 10 + 5 = {sum_val}")
print(f"Subtraction: 20 - 8 = {diff}")
print(f"Multiplication: 4 * 6 = {product}")
print(f"Division: 20 / 3 = {division}")
print(f"Floor Division: 20 // 3 = {floor_division}")
print(f"Exponent: 2^3 = {power}")
print(f"Modulo: 10 % 3 = {remainder}")

# Comparison operators
print(f"10 > 5 -> {10 > 5}")
print(f"10 == 5 -> {10 == 5}")
print(f"10 != 5 -> {10 != 5}")
print(f"3 < 7 -> {3 < 7}")

# Assignment operators
x = 10
x += 5
print(f"Assignment example: x += 5 => {x}")

# Logical operators
is_valid = True
has_access = False
print(f"Logical AND: {is_valid and has_access}")
print(f"Logical OR: {is_valid or has_access}")
print(f"Logical NOT: {not is_valid}")

# Identity operators
p = [1, 2, 3]
q = [1, 2, 3]
r = p
print(f"p is q -> {p is q}")
print(f"p is r -> {p is r}")

# Membership operators
letters = ["a", "b", "c"]
print(f"'b' in letters -> {'b' in letters}")
print(f"'z' not in letters -> {'z' not in letters}\n")


# ==========================================
# 3. CONDITIONAL STATEMENTS
# ==========================================
# Used to take decisions in code.
# Subtopics:
# - if
# - elif
# - else
# - nested if
# - ternary operator
# - match-case (Python 3.10+)

print("--- 3. Conditionals ---")

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print(f"Score: {score} => Grade: {grade}")

# Nested if example
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("You are eligible to vote.")
    else:
        print("You are adult but not a citizen.")
else:
    print("You are too young to vote.")

# Ternary operator example
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# match-case example
day = "Monday"

match day:
    case "Monday":
        print("Start of the work week.")
    case "Friday":
        print("Weekend is near!")
    case _:
        print("It is another day.")
print("")


# ==========================================
# 4. LOOPS
# ==========================================
# Loops repeat code multiple times.
# Subtopics:
# - for loops
# - while loops
# - range()
# - break
# - continue
# - nested loops

print("--- 4. Loops ---")

# For loop with range
print("For loop output:")
for i in range(5):
    print(f"  Loop iteration: {i}")

# For loop with list
fruits = ["apple", "banana", "cherry"]
print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# For loop with enumerate
for index, fruit in enumerate(fruits):
    print(f"  Index {index}: {fruit}")

# While loop
print("While loop output:")
counter = 3
while counter > 0:
    print(f"  Countdown: {counter}")
    counter -= 1

# Break example
print("Break example:")
for num in range(1, 10):
    if num == 5:
        print("Stopped at 5.")
        break
    print(num)

# Continue example
print("Continue example:")
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# Nested loops
print("Nested loops:")
for i in range(2):
    for j in range(3):
        print(f"  i={i}, j={j}")
print("")


# ==========================================
# 5. DATA STRUCTURES
# ==========================================
# Used to store collections of data.
# Subtopics:
# - Lists
# - Tuples
# - Sets
# - Dictionaries
# - Indexing, slicing, methods

print("--- 5. Data Structures ---")

# List
numbers = [10, 20, 30, 40]
numbers.append(50)          # add at end
numbers.insert(1, 15)       # insert at index 1
numbers.remove(30)          # remove an element
print(f"List after operations: {numbers}")
print(f"First item: {numbers[0]}")
print(f"Last item: {numbers[-1]}")
print(f"Sliced list: {numbers[1:4]}")

# List methods
numbers.sort()
print(f"Sorted list: {numbers}")
print(f"Length of list: {len(numbers)}")

# Tuple
coordinates = (10, 20)
print(f"Tuple: {coordinates}")
x_coord, y_coord = coordinates
print(f"Tuple unpacking: x={x_coord}, y={y_coord}")

# Set
set_numbers = {1, 2, 2, 3, 4}
print(f"Set removes duplicates: {set_numbers}")
set_numbers.add(5)
set_numbers.remove(2)
print(f"Set after change: {set_numbers}")

# Dictionary
student = {
    "name": "Yash",
    "age": 19,
    "course": "Python",
    "marks": [90, 85, 88]
}

print(f"Student name: {student['name']}")
print(f"Student course: {student.get('course')}")
student["city"] = "Delhi"
student["age"] = 20
print(f"Updated student: {student}")

# Loop through dictionary
for key, value in student.items():
    print(f"  {key}: {value}")
print("")


# ==========================================
# 6. FUNCTIONS
# ==========================================
# Functions are reusable blocks of code.
# Subtopics:
# - Defining functions
# - Parameters and arguments
# - Return values
# - Default arguments
# - Keyword arguments
# - *args and **kwargs
# - Lambda functions

print("--- 6. Functions ---")

def greet_user(username):
    """This function greets the user."""
    return f"Hello, {username}! Welcome back."

print(greet_user("Bob"))

# Function with multiple parameters
def add_numbers(a, b):
    return a + b

print(f"Addition result: {add_numbers(5, 7)}")

# Default parameter
def describe_pet(name, animal="dog"):
    return f"{name} has a {animal}."

print(describe_pet("Max"))
print(describe_pet("Luna", "cat"))

# Keyword arguments
def person_details(name, age, city):
    return f"{name} is {age} years old and lives in {city}."

print(person_details(name="Riya", age=21, city="Mumbai"))

# *args: variable number of positional arguments
def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(f"Sum with *args: {sum_all(1, 2, 3, 4, 5)}")

# **kwargs: variable number of keyword arguments
def print_info(**details):
    for key, value in details.items():
        print(f"  {key}: {value}")

print("User Details:")
print_info(name="Aman", role="Developer", city="Pune")

# Lambda function
square = lambda x: x * x
print(f"Lambda square of 6: {square(6)}")
print("")


# ==========================================
# 7. ERROR HANDLING
# ==========================================
# Helps prevent the program from crashing.
# Subtopics:
# - try
# - except
# - finally
# - multiple exceptions
# - raising custom exceptions

print("--- 7. Error Handling ---")

# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

# Multiple exceptions
try:
    value = int("abc")
except ValueError:
    print("Error: Value is not a valid integer.")

# Try except else finally
try:
    number = 25
    print(f"Square root of {number} = {number ** 0.5}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No errors occurred.")
finally:
    print("This always runs.")

# Raise your own exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age

try:
    print(check_age(-5))
except ValueError as e:
    print(f"Custom exception: {e}")
print("")


# ==========================================
# 8. FILE HANDLING
# ==========================================
# Reading and writing files.
# Subtopics:
# - open()
# - write mode
# - read mode
# - append mode
# - with statement
# - file existence
# - JSON file handling

print("--- 8. File Handling ---")

filename = "sample.txt"

# Write mode
with open(filename, "w") as file:
    file.write("Python is awesome!\nLearning is fun.\n")

print("Saved text to 'sample.txt'.")

# Read mode
with open(filename, "r") as file:
    content = file.read()
    print("Reading from file:")
    print(content)

# Append mode
with open(filename, "a") as file:
    file.write("This line was appended.\n")

# Read again
with open(filename, "r") as file:
    updated_content = file.read()
    print("Updated file content:")
    print(updated_content)

# Example: JSON writing
import json

data = {
    "name": "Yash",
    "age": 19,
    "skills": ["Python", "JavaScript"]
}

with open("student_data.json", "w") as file:
    json.dump(data, file)

with open("student_data.json", "r") as file:
    loaded_data = json.load(file)
    print(f"Loaded JSON data: {loaded_data}")

# Check if file exists
import os
print(f"Does file exist? {os.path.exists('sample.txt')}")
print("")


# ==========================================
# 9. EXTRA PRACTICE: SMALL SUMMARY
# ==========================================
# These are the core building blocks of Python:
# - variables
# - operators
# - conditions
# - loops
# - data structures
# - functions
# - error handling
# - file handling

print("--- 9. Quick Summary ---")
print("Python is easy to learn when you practice each concept with examples.")
print("Use variables for data, functions for reusable logic, loops for repetition,")
print("and file handling to save or read data.")

# Gaint primordial turtle: Incredibly
## NumPy (shorts for numerical Python ) is the foundational open source library for scientific computing and data analysis in Python . it provides the bckbone for almost every ,ajor Python data science and machine learning library , including Pandas, SciPy, Scikit-learn, and TensorFlow.

# 1. The Core Engine: The ndaaray
# At the heart of numpy is the ndaaray (N-dimensional array). Unlike Python lists, which can hold different data types and are scattered across your computer's memory, NumPy arrays are homogenous (all elements must be the exact same data type) and stored in a continous block of memory.

# Feature         Python Lists                   Numpy Arrays
# Data Types      Mixed types allowed (integers  Strict single 
#                 strings ,float together
# FeaturePython ListsNumPy ArraysData TypesMixed types allowed (integers, strings, floats together).Strict single type (e.g., all int64 or all float32).Memory AllocationScattered references (slower to look up).Contiguous block (highly optimized for hardware).Mathematical OperationsRequires explicit loops or list comprehensions.Native element-wise operations (Vectorization).SpeedSlow for large datasets.Extremely fast (written in optimized C).

# 2. Key Concepts and Terms 
# Vectorization: The process of performing mathematical operations on entire arrays at once without writing explict for loops in Python.
# Broadcastiong: A powerful mechanism that allows NumPy to perform operations on arrays of different shapes during arithmatic operations. For Examples, adding a single scalar number to a 2D matrix will automatically "broadcast"  that number acrossevery element.
# Data Types (dtype ): NumPy gives you precise control over how numbers are stored in memory (np.int8, np.int64, np.float32, np.complex128), which is crucial for optimizing performance and memory usage 

# 3. Essential Operations Cheat Sheet 
# Giant Primordial Turtle: Incredibly Intelligent

#Python 

import numpy as np

# From a list
arr = np.array([1, 2, 3])

# Arrays filled with zeros, ones, or placeholders
zeros = np.zeros((3, 3))        # 3x3 matrix of 0.0
ones = np.ones((2,4))           # 2x4 matrix of 1.0
empty = np.empty((2,2))         # Uninitialized memory (fastest)

# Sequence and intervals 

matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(matrix.shape)   # Output: (2, 3) - 2 rows, 3 columns
print(matrix.ndim)    # Output: 2 - Two dimensions
print(matrix.dtype)   # Output: int64 (or int32 depending on OS)

# Change shape (must have the same total number of elements)
flat = matrix.reshape(6) 
