class Car:

    def __init__(self, make, model, reg_num, num_doors, current_speed, max_speed, fuel_level):
        self.make = make
        self.model = model
        self.reg_num = reg_num
        self.num_doors = num_doors
        self.current_speed = current_speed
        self.max_speed = max_speed
        self.fuel_level = fuel_level

    def accelerate(self, amount):
        if self.current_speed + amount <= self.max_speed:
            self.current_speed += amount
            self.fuel_level -= 1

    def brake(self, amount):
        self.current_speed -= amount

    def refuel(self):
        self.fuel_level += 1
