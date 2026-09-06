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
my_tuple[2][0] = 99    # Valid! Tuple becomes (1,2,[99,4])
# my_tuple[0] = 5        # Throws TypeError     

"""
3. Core Operations & Built-in Methods
Tuples support fewer methods than lists due to their immutability.
Basic Operations

Concatenation (+): Combines two tuples into a new one. (1, 2) + (3, 4) → (1, 2, 3, 4)

Repetition (*): Repeats a tuple. (1, 2) * 2 → (1, 2, 1, 2)

Membership (in / not in): Checks if an item exists. 1 in (1, 2) → True
Built-in Methods
Tuples only have two built-in methods:
1. count(value): Returns the number of times a value appears.
index(value): Returns the first index where the value is found (raises ValueError if missing).
Built-in Functions
len(t): Returns total length.
max(t) / min(t): Returns highest/lowest item (elements must be of compatible types).
tuple(iterable): Converts an iterable (like a list or string) into a tuple.


4. Packing and Unpacking
Packing: Assigning multiple values to a single tuple variable.
python
"""
packed = 10, 20, 30  # Parentheses are optional here
# Use code with caution.Unpacking: Extracting tuple values back into variables.
# python
a, b, c = packed  # a=10, b=20, c=30
# Extended Unpacking (* operator):
# python
a, *b, c = (1, 2, 3, 4, 5) # a=1, b=[2, 3, 4], c=5