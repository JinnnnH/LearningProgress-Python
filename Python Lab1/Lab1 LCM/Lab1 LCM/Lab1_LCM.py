#This program prints the lowest common miltiple(LCM) of 2 numbers
import math                                                             #import math library for math.gcd()

num1 = int(input("Please enter num1: "))                                #ask for the first number
num2 = int(input("Please enter num2: "))                                #ask for the second number
gcd = math.gcd(num1, num2)                                              #get the greatest common divisor(GCD) by math.gcd()
LCM = (num1*num2)/gcd                                                   #LCM = the multiple of 2 numbers divided by GCD
print("The lowest common mulitple of the 2 number is ", LCM)            #print the result