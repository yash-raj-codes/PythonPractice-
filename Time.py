import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
hour = int(time.strftime('%H'))
print(hour)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

if(hour>=0 and hour < 12):
    print("Good morning Sir!")
elif(hour>=12 and hour <17):
    print("Good Afternoon Sir!")
else:
    print("Good Night Sir!")