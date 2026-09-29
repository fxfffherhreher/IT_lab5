class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)

    def show_all(self):
        result = []
        for vehicle in self.vehicles:
            result.append(vars(vehicle))
        return result

    def find_by_brand(self, brand):
        result = []
        for vehicle in self.vehicles:
            if vehicle.brand == brand:
                result.append(vars(vehicle))
        return result