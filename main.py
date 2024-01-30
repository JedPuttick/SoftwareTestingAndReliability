from car import Car

car1 = Car("Skoda", "Fabia", "GR07 THO", 5, 4, 1.2, 0, 102, 100)
car2 = Car("Porsche", "944", "OG23 SEP", 5, 4, 2.5, 0, 140, 100)

listOfCars = [car1, car2]

print("\nFirst Car: " f'{ car1.make, car1.model, car1.num_plate, car1.doors, car1.wheels, car1.engine_size, car1.current_speed, car1.max_speed, car1.fuel_level}')
print("\nSecond Car: " f'{ car2.make, car2.model, car2.num_plate, car2.doors, car2.wheels, car2.engine_size, car2.current_speed, car2.max_speed, car2.fuel_level}')

car1.accelerate(50)
print(f'\nAfter accelerating, the first car has a speed of {car1.current_speed}mph and a fuel level of {car1.fuel_level}%')

car1.brake(20)
print(f'\nAfter breaking, the first car has a speed of {car1.current_speed}mph and a fuel level of {car1.fuel_level}%')

car1.refuel(10)
print(f'\nAfter refueling, the first car has a fuel level of {car1.fuel_level}%')

print(listOfCars)
carSelection = int(input("What car would you like to select? [1] or [2]: "))
