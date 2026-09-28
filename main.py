from models.vehicle import Vehicle

car = Vehicle('BMW', 'M5', 2025)
bike = Vehicle('Cube', 'Nuroad', 2025)


print(car.get_info())
car.accelerate(50)
print(car.get_info())
car.brake(50)
print(car.get_info())
car.brake(15)