from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck

car1 = Car('BMW', 'M5', 2025, 4)
moto = Motorcycle('Suzuki', 'Hayabusa', 2018, 0)
truck = Truck('Belaz', 'max', 2026, 280)

vehicles = [car1, moto, truck]

for elem in vehicles:
    print(elem.move())
    print(elem.get_info())