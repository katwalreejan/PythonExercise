import random

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



car = Car("ABC-123", 142)

print("Initial Car Properties:")
print("Registration:", car.reg_number)
print("Max Speed:", car.max_speed, "km/h")
print("Current Speed:", car.current_speed, "km/h")
print("Travelled Distance:", car.distance, "km\n")


car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print("After accelerations (+30, +70, +50):")
print("Current Speed:", car.current_speed, "km/h")

car.accelerate(-200)  # Emergency brake
print("After emergency brake (-200):")
print("Current Speed:", car.current_speed, "km/h\n")


car.current_speed = 60
car.distance = 2000
car.drive(1.5)
print("After driving 1.5 hours at 60 km/h:")
print("Travelled Distance:", car.distance, "km\n")


cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    cars.append(Car("ABC-" + str(i), max_speed))

race_on = True
while race_on:
    for c in cars:
        c.accelerate(random.randint(-10, 15))
        c.drive(1)
        if c.distance >= 10000:
            race_on = False
            break

print("\n--- Race Results ---")
print("Reg.No   MaxSpeed   CurrSpeed   Distance")
for c in cars:
    print(f"{c.reg_number:<8} {c.max_speed:<9} {c.current_speed:<10} {c.distance:.1f}")
