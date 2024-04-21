print("WELCOME TO THE BMI CALCULATOR")
height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kilograms: "))

bmi = weight / (height * height)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you might be slightly overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")
