#Exercise 6.1
import random

def roll_dice():
    return random.randint(1, 6)

while True:
    result = roll_dice()
    print("You rolled:", result)
    if result == 6:
        break


#Exercise 6.2
def roll_dice():
    return random.randint(1, sides)

sides = int(input("Enter the number of sides on the dice: "))
while True:
    result = roll_dice()
    print("You rolled:", result)
    if result == sides:
        break


#Exercise 6.3
def convert_to_liters(gallons):
    return gallons * 3.78541

while True:
    gallons = float(input("Enter volume in gallons: "))

    if gallons < 0:
        print("Program ended.")
        break

    liters = convert_to_liters(gallons)
    print("That is", liters, "liters.")


#Exercise 6.4
def sum_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

my_list = [3, 5, 7, 2, 8,9]

result = sum_list(my_list)
print("The sum of the list is:", result)


#Exercise 6.5
def rem_odd_numbers(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = rem_odd_numbers(original_list)

print("Original list:", original_list)
print("List without odd numbers:", filtered_list)

#Exercise 6.6
import math

def pizza_unit_price(diameter_cm, price_euros):
    radius_m = (diameter_cm / 2) / 100
    area = math.pi * (radius_m * radius_m)
    unit_price = price_euros / area
    return unit_price

diameter1 = float(input("Enter diameter of first pizza (cm): "))
price1 = float(input("Enter price of first pizza (euros): "))

diameter2 = float(input("Enter diameter of second pizza (cm): "))
price2 = float(input("Enter price of second pizza (euros): "))

unit_price1 = pizza_unit_price(diameter1, price1)
unit_price2 = pizza_unit_price(diameter2, price2)

print(f"Unit price of first pizza is {unit_price1:.2f}, euros per square meter")
print(f"Unit price of second pizza is {unit_price2:.2f}, euros per square meter")

if unit_price1 < unit_price2:
    print("First pizza is better value for money.")
elif unit_price2 < unit_price1:
    print("Second pizza is better value for money.")
else:
    print("Both pizzas give the same value for money.")
