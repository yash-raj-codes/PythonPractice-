a = int(input("Enter your age: "))
print("Your age is:", a)

# conditional operators
# >, <, >=, <=, ==, !=

print(a>18)
print(a<=18)
print(a==18)
print(a!=18)

if(a>18):
    print("You can drive")
else:
    print("You cannot drive")
print("Yay!")

applePrice = 210
budjet = 200
if(applePrice <= budjet):
    print("Alexa, addd 1kg Apples to the cart.")
else:
    print("Alexa, do not add apples to the cart")

#   Logging into the

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

x = int(input("Enter the value of x: "))
# x is the variable to match 
match x:
    #if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _:
        print(x)

i = "Yash Raj"
for a in i:
    j = i + a
    print(a)
    for a in j:
        z = j + i
        print(j)
        for a in z:
            print(z)
