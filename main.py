from car import Car

car1 = Car("Ford", "Fiesta", "AB12CDE", 4, 0, 10, 10)
car2 = Car("Honda", "Jazz", "XY99ZZZ", 5, 0, 8, 11)

print(f"Car 1 is a {car1.make} {car1.model}. Car 2 is a {car2.make} {car2.model}.")
print(f"Car 1 speed is {car1.current_speed}, Car 1 fuel level is {car1.fuel_level}")

car1.accelerate(3)
car1.accelerate(5)
car1.brake(2)

print(f"Car 1 speed is {car1.current_speed}, Car 1 fuel level is {car1.fuel_level}")
