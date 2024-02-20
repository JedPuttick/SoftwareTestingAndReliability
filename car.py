class Car:

    def __init__(self, make, model, num_plate, doors, wheels, engine_size, current_speed, max_speed, fuel_level, type):
        if max_speed < 1:
            raise Exception("Max speed cannot be less than 1")
        elif doors < 1:
            raise Exception("There cannot be fewer than 1 door")
        elif wheels < 3:
            raise Exception("There cannot be fewer than 3 wheels")
        self.make = make
        self.model = model
        self.num_plate = num_plate
        self.doors = doors
        self.wheels = wheels
        self.engine_size = engine_size
        self.current_speed = current_speed
        self.max_speed = max_speed
        self.fuel_level = fuel_level
        self.type = type

    def __repr__(self):
        return f'{self.make} {self.model} ({self.num_plate})'

    def accelerate(self, increase):
        if self.fuel_level == 0:
            print("The car has run out of fuel, acceleration not possible")
            return False

        if self.current_speed + abs(increase) >= self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed += abs(increase)

        if self.fuel_level - abs(increase) * 0.1 >= 0:
            self.fuel_level -= abs(increase) * 0.1
        else:
            diff = -(self.fuel_level - abs(increase) * 0.1)
            self.current_speed = self.current_speed - diff * 10
            self.fuel_level = 0

    def brake(self, decrease):
        if self.current_speed - abs(decrease) <= 0:
            self.current_speed = 0
        else:
            self.current_speed -= abs(decrease)

    def refuel(self, fuel_increase):
        if self.fuel_level + abs(fuel_increase) >= 100:
            self.fuel_level = 100
        else:
            self.fuel_level += abs(fuel_increase)
