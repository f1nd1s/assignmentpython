import csv
from models import Car
class AdminFunctions:
    def __init__(self):
        admin = "Ilyas"
        pass

    def add_car_to_csv(self, car):
        try:
            with open("cars.csv", 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([car.car_number, car.mark, car.model, car.year, car.price])
            print("Car information added to CSV file successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def read_cars_from_csv(self):
        cars = []
        try:
            with open("cars.csv", 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    car = Car(row[0], row[1], row[2], row[3], row[4])
                    cars.append(car)
            return cars
        except FileNotFoundError:
            print(f"File not found")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
