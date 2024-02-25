from models import Car
from menufp import UserService
from AdminFunctions import AdminFunctions
admin_function = AdminFunctions()
service = UserService()
import csv


print("Welcome to our Car Sharing Service")
while True:
    print("1. Login.")
    print("2. Register.")
    choice = input("Enter your choice: ")
    if choice == "1":
        login = input("Please enter your login: ")
        password = input("Please enter your password: ")
        if service.login(login, password):
            print(f"{login} login successfully!")
            break
        else:
            print(f"{login} does not exist")


    elif choice == "2":
        login = input("Please enter your login: ")
        password = input("Please enter your password: ")
        service.register(login, password)

    print("\n")

if login == "Ilyas" and password == "1234":
    while True:
        print("1. Add new car")
        print("2. Purchase history")
        print("3. Show all cars")
        print("4. Exit")
        choice = input("Enter your choice: ")
        print("\n\n")
        if choice == "1":
            car_number = input("Enter car number: ")
            marks = input("Enter marks: ")
            model = input("Enter model: ")
            year = input("Enter year: ")
            price = input("Enter price: ")
            car = Car(car_number, marks, model, year, price)
            admin_function.add_car_to_csv(car)

        if choice == "3":
            cars = (admin_function.read_cars_from_csv())
            del cars[0]
            if cars:
                print("All our Cars are")
                for car in cars:
                    print("\t" + car.__str__())

        if choice == "4":
            break

        print("\n\n")


while True:
    print("1. Show all cars.")
    print("2. Rent car.")
    choice = input("Enter your choice: ")
    if choice == "1":
        cars = (admin_function.read_cars_from_csv())
        del cars[0]
        if cars:
            print("All our Cars are")
            for car in cars:
                print("\t" + car.__str__())

    elif choice == "2":
        login = input("Please enter your login: ")
        password = input("Please enter your password: ")
        if service.login(login, password):
            car_number = input("Which car do you want to rent(car number)")
            service.rent_car(login, password, car_number)
            pass

    print("\n")
