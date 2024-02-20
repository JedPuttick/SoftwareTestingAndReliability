class CarPark:

    def __init__(self, capacity = 15, bike_capacity = 4):
        self.capacity = capacity
        self.bike_capacity = bike_capacity
        self.cars = []
        self.bikes = []
        self.barrier_open = False

    def add_vehicle(self, vehicle):
        if vehicle.type == "car" or vehicle.type == "emergency":
            if len(self.cars) == self.capacity and vehicle.type != "emergency":
                print("car park full")
                self.barrier_open = False
                return
            for car in self.cars:
                if car == vehicle:
                    print("Vehicle already in car park")
                    self.barrier_open = False
                    return
            print(f"{vehicle.num_plate} has entered the car park")
            self.cars.append(vehicle)
        elif vehicle.type == "bike":
            if len(self.bikes) == self.bike_capacity:
                print("car park full")
                return
            for bike in self.bikes:
                if bike == vehicle:
                    print("Vehicle already in car park")
                    return
            print(f"{vehicle.num_plate} has entered the car park")
            self.bikes.append(vehicle)
        else:
            print(f"Vehicles of type '{vehicle.type}' not allowed in car park")
    def remove_car(self, plate):
        for car in self.cars:
            if car == plate:
                self.cars.remove(car)
            print(f"{plate} has left the car park")