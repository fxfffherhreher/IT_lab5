from models.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, brand, model, year, max_load):
        super().__init__(brand, model, year)
        self.max_load = max_load

    def get_info(self):
        return f"Грузовик: {self.brand} {self.model}, Максимальная загрузка: {self.max_load}"

    def move(self):
        return "Грузовик движется"