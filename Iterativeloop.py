#Exercise 5.1
import random

dice_count = int(input("How many dice to roll? "))
total = 0

for i in range(dice_count):
    roll = random.randint(1, 6)
    total += roll

print("Total sum of dice rolls:", total)


#Exercise 5.2
numbers = []

while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    number = float(user_input)
    numbers.append(number)

numbers.sort(reverse=True)  # Sort descending

print("Five greatest numbers:")
for num in numbers[:5]:
    print(num)


#Exercise 5.3
number = int(input("Enter an integer: "))

if number < 2:
    print("Not a prime number.")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


#Exercise 5.4
cities = []

for i in range(5):
    while True:
        city = input(f"Enter city name {i+1}: ")
        if city == "":
            print("Empty input is not allowed. Please enter a city name.")
        elif city.isdigit():
            print("Numbers are not allowed. Please enter a valid city name.")
        else:
            cities.append(city)
            break

print("\nCities you entered:")
for city in cities:
    print(city)




