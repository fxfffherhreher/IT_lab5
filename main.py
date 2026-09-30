from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck
from garage import Garage
from models.bus import Bus

def main():
    car1 = Car('BMW', 'M5', 2025, 5)
    car2 = Car('Suzuki', 'Swift', 2020, 5)
    moto = Motorcycle('Suzuki', 'Hayabusa', 2018, 0)
    truck = Truck('Belaz', 'max', 2026, 280)
    school_bus = Bus('Blue Bird', 'All American', 2013, 84, 'yellow')

    garage = Garage()
    garage.add_vehicle(car1)
    garage.add_vehicle(car2)
    garage.add_vehicle(moto)
    garage.add_vehicle(truck)
    garage.add_vehicle(school_bus)

    print(garage.show_all())
    


if __name__ == "__main__":
    main()