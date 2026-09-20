"""Python Docstrings Are the string literals that appear right after the defination of a function, method, class, or module."""

'Example : '

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)

'''
\"Takes in a number n, returns the square of n\" is a docstring which will not appear in the output
'''

print(square.__doc__)

def factorial(num):
    if (num == 1 or num ==0):
        return 1
    else:
        return(num*factorial(num-1))

# Driver code
num = 7
print("Number: ", num)
print("Factorial: " ,factorial(num))


# Python sets
s = {2,4,2,6}
print(s)

info={"Carla", 19, False, 5.9, 19}
print(info)

harry = {}
print(type(harry))

for value in info:
    print(value)


# Operations on sets
"""Sets in the python more or less work in the same way as in the mathematics. We can perform operations like union and intersection on the sets just like in mathematics"""

s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))     # {1,2,3,5,6,7}
print(s1,s2)        # s1 and s2 untouched hien rahen