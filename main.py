from models.vehicle import Vehicle

car = Vehicle('BMW', 'M5', 2025)
bike = Vehicle('Cube', 'Nuroad', 2025)

print(vars(car))
print(vars(bike))

bike.year = 2026


print(vars(car))
print(vars(bike))