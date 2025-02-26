import time
Time = time.strftime('%H:%M:%S')
print(Time)
mornig = 5
afternoon = 12
evening = 18
Time = int(time.strftime('%H'))
print(type(Time))
if(Time > mornig and Time < afternoon):
    print("Good Mornig Nahid")
elif(Time > afternoon and Time < evening):
    print("Good Afternoon Nahid")
elif(Time > evening):
    print("Good Evening Nahid")