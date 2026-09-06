"""
1. Introduction to Tuples
A Tuple is a built-in data structure in Python used to collect ordered collection of items.

* Syntax: Items are enclosed within parentheses () and seperated by commas , .
* Key Characteristics:
 *Ordered: Elements have defined order that will not change.
 *Immutable: Once created elements cannot be added,removed, or modified.
 * Allows Duplicate: Can hold identical values.
 * Hetrogeneous: Can store multiple data types(e.g., integers, strings, floats) together.

2. Core Mechanics & Syntax Gotchas
The Single-Element Tuple Trap
To create a tuple only with element, you must include a trailing comma.
"""

# python 
t1 = (5) # Type: int
t2 = (5,) # Type: tuple(Correct!)
print(t1 , t2, sep = '\n', end = '\n'*2)

"""
The Immutable Exception (Mutable Elements Inside a Tuple)

While a tuple itself cannot be altered, if it contains a mutable object(like a list), the contents of that mutable object cannit be modified.
"""

# python

my_tuple = (1,2,[3,4])
my_tuple(2)[0] = 99    # Valid! Tuple becomes (1,2,[99,4])
# my_tuple[0] = 5        # Throws TypeError     