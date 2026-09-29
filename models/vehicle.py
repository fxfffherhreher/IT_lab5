from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._speed = 0

    def accelerate(self, value):
        self.speed += value

    def brake(self, value):
        self.speed -= value

    def stop(self):
        self._speed = 0

    def get_info(self):
        return vars(self)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Скорость не может быть отрицательной")
        self._speed = value

    def __str__(self):
        return f'{self.brand} {self.model} {self.year}, скорость: {self.speed} км/ч'