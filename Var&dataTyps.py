"Variables in the Python "
"Programming"
"Machine<---Translator(Compiler/Interpreter)<---Code(Python)"

"Python is said to be an High Level Language(HLL)"

"""Python is simple and easy 
Free & Open Source
High Level Language
Developed by Guido van Rossum
Portable
"""

print("Hello Yash!")

"Python Character Set"
"Letters - A to Z, a to z"
"Digits - 0 to 9"
"Special Symbols - + - * / etc"
"Whitespaces - Blank Space, tab, carriage return, newline, formfeed"
"Other characters - Pyhton can process all ASCII and Unicode characters as part of data or literals"

print("Yash is my name.\nMy age is 19.")
print(19)
print(35+19)

"Variables :- A variable is a name given to a memory location in a program."

name = "Yash"
age = 19
price = "25.99"
print(name, age , price, sep = ",  ")

name = "Harsh"
age = 33
price ="22"
print(name, age , price, sep = ",  ")

name = 15
age = "age"
price = 2
print(name, age , price, sep = ",  ")


length = int(input("Length : "))
width = int(input("Width : "))
# The fake prince was exposed. 36
print("Area of rectangle by given length and width is :", length*width)

a = None 
print(type(a))  # None Type

old = False
print(old)
print(type(old)) # Bool Type

""" Keywords are
and                 else        in          return
as                  except      is          True
assert              finally     lambda      try
break               False       nonlocal    with
class               for         None        while
continue            from        not         yield
def                 global      or
del                 if          pass
elif                import      raise
"""
num1 = 34
num2 = 33
print(num1+num2)


# This is a comment. It takes 0 bytes of RAM.
    
"""This is a docstring. 
It is saved in memory and takes up RAM space.
"""
print(num1 == num2)
print(num1 != num2)

#type conversion
a = "3"
b = 4.25

sum = int(a) + b
print(sum)

aa = input()
ab = int(input())
ac = float(input())
ad = bool(int(input()))
print(aa,ab,ac,ad,sep="\n")