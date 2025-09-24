airport_data = {}

while True:
    print("What do you want to do?")
    print("1 - Add a new airport")
    print("2 - Get airport information")
    print("3 - Quit")

    choice = input("Enter your choice (1 or 2 or 3): ")

    if choice == "1":
        icao = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airport_data[icao] = name
        print("Airport added.")

    elif choice == "2":
        icao = input("Enter ICAO code to search: ")
        if icao in airport_data:
            print("Airport name:", airport_data[icao])
        else:
            print("Airport not found.")

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Please enter a valid choice.")
