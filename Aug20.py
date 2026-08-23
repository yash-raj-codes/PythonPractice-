# num = int(input("Input a number(-1 to stop):"))

# while num != -1:
#     print("You entered:", num)
#     num = int(input("Enter a number(-1 to stop):"))


# Practice 1
marks = 0
num = 0
turns = 0
while (marks>=0):
    
    num = int(input("Marks in the subjects(-1 if completed)"))
    if (num == -1):
        break
    elif(num != -1):
        marks += num
        turns += 1

print(marks/(turns))