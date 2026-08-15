x = 3
print(type(x))

y = 15.5
print(type(y))

a=b=c=10
print(type(a))
print(type(b))
print(type(c) , end ='\n'*2)

print(a+x)
print(a-x)
print(a*x)
print(a/x)
print(a//x)
print(a%x)
print(a**x , end ='\n'*2)

print(x==a)
print(x>=a)
print(x<=a)
print(x==a , end ='\n'*2)

x*= 2
print(x)
x/= 2
x/= 2
print(x , end ='\n'*2)

age = 22
citizen = True

print(age >= 18 and citizen)
print(age <= 18 or citizen)
print(not citizen , end ='\n'*2)

fruits = ["Apple", "Mango", "Banana"]

print("Apple" in fruits)
print("Orange" not in fruits)
print("Banana" not in fruits)