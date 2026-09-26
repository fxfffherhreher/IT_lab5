from models.vehicle import Vehicle

car = Vehicle('BMW', 'M5', 2025)
bike = Vehicle('Cube', 'Nuroad', 2025)

print(car._speed)
car.accelerate(20)
print(car._speed)
car.brake(10)
print(car._speed)
car.stop()
print(car.get_info())