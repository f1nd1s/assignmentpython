
class Vehicle:
    def __init__(self, mark, model, year, price):
        self.mark = mark
        self.model = model
        self.year = year
        self.price = price


class Car(Vehicle):
    def __init__(self, car_number, mark, model, year, price):
        super().__init__(mark, model, year, price)
        self.car_number = car_number


    def __str__(self):
        return f'{self.car_number} | {self.mark} {self.model}, {self.year}, {self.price}$ per day'
