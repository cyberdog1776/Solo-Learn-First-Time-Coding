#BMI Calculator
#print("Enter your weight in kilos: ")
weight_kilos = int(input())
#print("Enter your height in meters: ")
height_meters = float(input())
BMI = weight_kilos/(height_meters**2)
#print("Enter your height in meters: ")
if BMI < 18.5:
    print("Go Eat!")
elif BMI >= 25:
    print("Normal")
elif BMI >= 30:
    print("Overweight")
else:
    print("Fat As Fuck!")
 