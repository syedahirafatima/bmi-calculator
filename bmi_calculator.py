# BMI calculator

# input weight in kilograms
weight = float(input("Enter your weight in kilograms: "))

# input height in meters
height = float(input("Enter your height in meters: "))

# calculate BMI
bmi = weight / (height * height)

# display result
print("Your BMI is:", bmi)

# interpret BMI
if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 24.9:
    print("You have a normal weight.")
elif bmi >= 25 and bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
