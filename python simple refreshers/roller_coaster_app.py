print ("welcome to the roller coaster app")
height = int (input("please input your height in metres"))

if height >= 120:
    print ("You can ride the roller coaster")
    age = int(input("please input your age"))
    if age <12:
        print ("please pay 5$!")
    elif age <=18:
        print("please pay 10 $")
else:
    print("sorry, you need to grow taller to ride the roller coaster")