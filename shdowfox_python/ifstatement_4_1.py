h=float(input("enter height in meters:"))
w=int(input("enter weight in kilograms:"))
BMI=(w)/(h**2)

if (BMI>=30):
    print("Obesity")

elif(25<=BMI<30):
    print("Overweight")

elif(18.5<=BMI<25):
    print("Normal" )

else:
    print("Underweight" )


