# range(start, stop,step)
for i in range(5):
    print(i)

# range(5) generates numbers from 0 to 4, not 0 to 5

numbers = list(range(1,6))
print(numbers)

print(list(range(5)))  # 0,1,2,3,4
print(list(range(2,8))) # 0,1,2,3,4
print(list(range(1,10,3)))  # 1,4,7
print(list(range(10,0,-2))) # 10, 8, 6, 4, 2

for i in range(1,6):
    print(i)

for ch in "python":
    print(ch)

for i in range(1,4):
    for j in range(1,4):
        print(i,j)

print("")
print("")
print("")

i = 1
while i <= 5:
    print(i)
    i += 1

print("")
print("")

for i in range(1,11):
    if i == 5:
        break
    print(i)

print("")
print("")
print("")

for i in range(1,11):
    if i == 5:
        continue
    print(i)

print("")
print("")

for i in range(1,6):
    if i== 3:
        pass
    print(i)

print("")
print("")

age = 20
if age >= 18:
    pass
else:
    print("Not eligible")

# Here, pass means do nothing when the condition is true
