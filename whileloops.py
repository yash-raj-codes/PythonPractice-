for i in range(3):
 print(i)
print()

i = 0
while(i<=3):
    print(i)
    i = i+1
print()
print("Done with the loop")
print()

i = int(input("Enter the number: "))
while(i<=38):
    i = int(input("Enter the number: "))
    print(i)
print()

count = 5
while(count > 0):
    print(count)
    count -= 1
else:
    print("I am inside else")

'''
do {
    #  loop body;
}while(condition)
'''

for i in range(12):
   if(i==5):
      print("Skip the iteration")
      continue
   if(i==10):
      break
   print("5 X", i+1, "=" ,5 * (i+1))

i = 0
while True:
   print(i)
   i = i + 1
   if(i%100 == 0):
      break

def calculateGmean(a,b):
   mean = (a*b)/(a+b)
   print(mean)

def isGreater(a,b):
    if(a>b):
      print("First number is Greater")
    elif (b>a):
      print("Second number is Greater")
    else:
       print("Both numbers are equal")

def isLesser(a,b):
   pass

a = 9
b = 8
# gmean1 = (a*b)/(a+b)
# print(gmean1)
isGreater(a,b)
calculateGmean(a,b)

c = 5
d = 7
# gmean2 = (c*d)/(c+d)
# print(gmean2)
isGreater(c,d)
calculateGmean(c,d)

# while True:
#     pass  # An infinite loop that does nothing

print("Yash")

def average(a=4,b=8):
   print("The average is ", (a+b)/2)

# average(4, 6)
average(b = 9)
average(a = 21)

average(5,7)

def avg(*numbers):
#    print(type(numbers))
    sum = 0
    for i in numbers:
      sum = sum + i
      print("Average is: ", sum/len(numbers))

avg(5,6,7,8)

marks = [3,5,6]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])
# print(marks[6])

marks[1] = 4
print(marks)

if "6" in marks:
   print("Yes")
else:
   print("No")


if "arry" in "Harry":
   print("Yes")

l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
l.append(7)
l.sort(reverse=True)
l.reverse
print(l.index(1))
print(l.count(1))

m = l
m[0] = 0
print(l)

m = [900,100,1100]
k = l+m
l.extend(m)
print(l)

tuple1 = (0,1,2,3,2,3,1,3,2,3)
res = tuple1.count(3) 
res = tuple1.index(3)
res = tuple1.index(3)
print('Count of 3 tuple1 is: ', res)

