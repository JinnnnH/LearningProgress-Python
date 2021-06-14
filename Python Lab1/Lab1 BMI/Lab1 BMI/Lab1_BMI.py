#This program gives your BMI
height = float(input("Please input your height in meters: "))           #inputs can be in float
weight = float(input("Please input your weight in kg: "))               #inputs can be in float

BMI = weight/(height**2)                                                #BMI = weight / height^2
print("Your BMI is: ", BMI)