'First Program' 

# In this writing a comment in sigle line.

print("Python")     #Prints Pyhton

"""
This is also used
for multi line comment
"""
'single time its works also but for single line only not multi lines'

print('Hello')      #Prints Hello in the next line

'Variables in python'
'A variables stores data'

name = "John"
age = 20
Age = 25            # Case Specific
marks = 89.5
boolExample = True
sum = age + Age

print(name)
print(age,Age,sum , sep=', ',end =' '+'\n'*3)
print(marks)
print(boolExample)

'Rules for naming variables'
student_name = "Ram"
marks1 = 90
# _name = "Yash"      cannot use these
# class = 10
# student-name = "Yash"

print(student_name, marks1,sep =", ",  end = '\n'*2)
print(type(age))
print(type(name))
print(type(boolExample))
print(type(marks), end ='\n'*2)

'string data type'
name2 = "Alice"
print(name2)

first = "Hello"
second = "Python"
print(first + " " + second , end = '\n'*3)

age2 = 17
print(age2 >= 18)