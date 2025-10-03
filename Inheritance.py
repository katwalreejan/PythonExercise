
class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)  # call parent initializer
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Book: {self.name}, Author: {self.author}, Pages: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Magazine: {self.name}, Chief Editor: {self.chief_editor}")


# === Test Publications ===
donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
compartment = Book("Compartment No. 6", "Rosa Liksom", 192)

donald_duck.print_information()
compartment.print_information()



class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, battery_capacity):
        super().__init__(reg_number, max_speed)  # call Car initializer
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, tank_volume):
        super().__init__(reg_number, max_speed)
        self.tank_volume = tank_volume



electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)


electric.accelerate(120)
gasoline.accelerate(150)


electric.drive(3)
gasoline.drive(3)

print(f"\nElectric Car {electric.reg_number} travelled {electric.distance} km")
print(f"Gasoline Car {gasoline.reg_number} travelled {gasoline.distance} km")
