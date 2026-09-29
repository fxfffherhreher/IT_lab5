from models.vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        return f"Мотоцикл: {self.brand} {self.model}, коляска: {self.doors}"

    def move(self):
        return "Мотоцикл движется"