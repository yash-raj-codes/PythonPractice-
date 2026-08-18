num = -10

if num >= 0:
    print("Positive")
else:
    print("Negetive")


year = int(input())
if(year&4==0):
    print("Leap year")
else:
    print("Not a leap year")

num = int(input())
if(num%10==0):
    print("Divisible by both 5 and 10")
elif (num%5==0):
    print("Divisible by 5 only")
else:
    print("Divisible by neither 5 nor 10")

