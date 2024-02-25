import csv
class UserService:
    def __init__(self):
        pass


    def register(self, login, password):
        try:
            with open('users.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([login, password])
            print("New User was loged successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def login(self, login, password):
        try:
            with open("users.csv", 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == login and row[1] == password:
                        return True
            return False
        except FileNotFoundError:
            print(f"File not found :(")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def view_user_info(self):
        print("User Information:")
        for login, password in self.users.items():
            print(f"Username: {login}, Password: {password}")
            
    def rent_car(self, login, password, car_number):
        try:
            with open("purchase.csv", 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([login, password, car_number])
            print(f"{login} rented {car_number} successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
        pass