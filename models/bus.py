from models.vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, brand, model, year, number_of_seats, color):
        super().__init__(brand, model, year)
        self.number_of_seats = number_of_seats
        self.color = color

    def get_info(self):
        return f"Автобус: {self.brand} {self.model}, мест: {self.number_of_seats}, цвет: {self.color}"
    
    def move(self):
        return "Автобус движется"
    