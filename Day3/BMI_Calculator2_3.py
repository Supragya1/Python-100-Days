height = float(input("Enter your height in meter \n"))
weight = int(input("Enter your weight in kgs \n"))
BMI = weight/height**2
# BMI = round(BMI,2)
if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI >= 18.5 and BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >= 25 and BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >= 30 and BMI < 35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")