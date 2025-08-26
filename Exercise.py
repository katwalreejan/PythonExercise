# Exercise 1
name="Reejan Katwal"
print(f"Hello, {name}!")

# Exercise 2.1
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Exercise 2.2
import math
radius = float(input("Enter the radius of a circle: "))
answer = math.pi * radius**2
print(f"Area : {answer:.2f}")

# Exercise 2.3
length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimeter = 2 * (length + width)
area=length*width
print(f"Perimeter : {perimeter:.2f}" )
print(f"Area : {area:.2f}")

# Exercise 2.4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
total=(a+b+c)
product=a*b*c
average=(a+b+c)/3
print(f"Sum : {total}")
print(f"Product : {product}")
print(f"Average : {average:.2f}")

# Exercise 2.5
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)
kg = int(grams // 1000)
g = grams % 1000
print(f"The weight in modern units:\n{kg} kilograms and {g:.2f} grams.")