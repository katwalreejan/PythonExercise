# Exercise 1
name="Reejan Katwal"
print(f"Hello, {name}!")

# Exercise 2.1
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Exercise 2.2
pi = 3.14159
radius = float(input("Enter the radius of a circle: "))
answer = pi * radius**2
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

#Exercise 3.1
length = int(input("Enter the length of the zander in cm: "))
if length < 42:
    print(f"Release the fish back in lake. It is {42 - length} cm below the size limit.")
else:
    print("The fish meets the size limit.")


#Exercise 3.2
cabin=input('Enter the class of cruise ship (LUX, A, B, C): ').upper()
if cabin == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin == "A":
    print("Above the car deck, equipped with a window.")
elif cabin == "B":
    print("Windowless cabin above the car deck.")
elif cabin == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")


#Exercise 3.3
gender = input("Enter biological gender (male/female): ").lower()
hemoglobin = int(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin value is low.")
    elif hemoglobin <= 155:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin value is low.")
    elif hemoglobin <= 167:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
else:
    print("Invalid gender.")



#Exercise 3.4
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year.")
elif year % 100 == 0:
    print("Not a leap year.")
elif year % 4 == 0:
    print("Leap year.")
else:
    print("Not a leap year.")


#Exercise 4.1
num = 1
while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1


#Exercise 4.2
inches = 0
while inches >= 0:
    inches = float(input("Enter the value in inches: "))
    if inches >= 0:
        print(inches, "inches =", inches * 2.54, "cm")

#Exercise 4.3
value = input("Enter a number: ")

if value == "":
    print("No numbers entered.")
else:
    smallest = float(value)
    largest = float(value)

    while value != "":
        number = float(value)
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
        value = input("Enter a number: ")

    print("The smallest number is:", smallest)
    print("The largest number is:", largest)


#Exercise 4.4
secret = 7
guess = 0
while guess != secret:
    guess = int(input("Guess the number between (1-10): "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct!")


#Exercise 4.5
correct_user = "python"
correct_pass = "rules"
attempts = 0
username = ""
password = ""

while attempts < 5:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == correct_user and password == correct_pass:
        print("Welcome")
        attempts = 5
    else:
        print("You have entered wrong credentials")
        attempts = attempts + 1

if username != correct_user or password != correct_pass:
    print("Access denied")


#Exercise 4.6
Point = int(input("Enter how many points to generate: "))
circle = 0
count = 0

while count < Point:
    x = (count % 100) / 50 - 1
    y = ((count * 3) % 100) / 50 - 1

    if x*x + y*y < 1:
        circle = circle + 1
    count = count + 1

pi_approx = 4 * circle / Point
print("Approximation of pi:", pi_approx)



