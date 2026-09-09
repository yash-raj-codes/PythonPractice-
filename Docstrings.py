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

#