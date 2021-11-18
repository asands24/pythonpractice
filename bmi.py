#input weight
weight = int(input("Enter weight in kilograms: "))
#input height
height = float(input("Enter height in inches: "))
#calculate BMI (weight/height^2)
x = float(weight/(height**2))

#decision if x is less than 18.5 print underweight
if (x < 18.5):
    print("Underweight")
#else, decision nested if x is equal to 18.5 and less than 25 print normal
elif (x <= 25):
    print("Normal")
#else, decision nested if x is equal to 25 and less than 30 print overweight
elif (x <= 30):
    print ("Overweight")
#else, decision nested if x is more than 30 print obesity
elif (30 < x):
    print("Obesity")
