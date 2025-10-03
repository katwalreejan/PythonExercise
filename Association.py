import random

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom  # start at bottom floor

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
        print("Elevator at floor", self.current_floor)

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
        print("Elevator at floor", self.current_floor)

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = []
        for _ in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nRunning elevator {elevator_number} to floor {target_floor}")
            self.elevators[elevator_number].go_to_floor(target_floor)

    def fire_alarm(self):
        print("\nFIRE ALARM! All elevators returning to bottom floor...")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i}:")
            elevator.go_to_floor(elevator.bottom)



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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print("\nRace Status:")
        print(f"{'Reg.No':<8} {'MaxSpeed':<9} {'CurrSpeed':<10} {'Distance':<10}")
        for car in self.cars:
            print(f"{car.reg_number:<8} {car.max_speed:<9} {car.current_speed:<10} {car.distance:<10.1f}")

    def race_finished(self):
        return any(car.distance >= self.distance for car in self.cars)


print("Elevator Test")
h = Elevator(1, 10)
h.go_to_floor(5)
h.go_to_floor(1)


print("\n Building Test")
b = Building(1, 10, 2)  # 2 elevators
b.run_elevator(0, 6)
b.run_elevator(1, 9)
b.fire_alarm()


print("\n Car Race Test")
cars = []
for i in range(1, 11):
    cars.append(Car("ABC-" + str(i), random.randint(100, 200)))

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"\nAfter {hours} hours")
        race.print_status()

print("\n Final Results")
race.print_status()
