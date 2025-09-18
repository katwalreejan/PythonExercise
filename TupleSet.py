#Exercise 7.1
seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter the number of a month: "))

if month in (12, 1, 2):
    season = seasons[0]
elif month in (3, 4, 5):
    season = seasons[1]
elif month in (6, 7, 8):
    season = seasons[2]
elif month in (9, 10, 11):
    season = seasons[3]
else:
    season = None

if season:
    print(f"The season is {season}.")
else:
    print("Invalid month. Please enter a number from 1 to 12.")


#Exercise 7.2
names = set()

while True:
    name = input("Enter a name: ")

    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nList of names entered are:")
for name in names:
    print(name)
