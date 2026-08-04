# ----------- Question 1 -----------

class Engine:

    def start(self):
        print("Engine Started Successfully.")


class Car:

    def __init__(self):
        self.engine = Engine()

    def drive(self):
        print("Car is Ready.")
        self.engine.start()
        print("Car is Moving.")


car = Car()

car.drive()


# ----------- Question 2 -----------

class Engine:

    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        print(f"{self.engine_type} Engine Started Successfully.")


class Car:

    def __init__(self, brand, engine_type):
        self.brand = brand
        self.engine = Engine(engine_type)

    def drive(self):
        print("\n========== Car Details ==========")
        print(f"Brand: {self.brand}")
        self.engine.start()
        print(f"{self.brand} Car is Moving.")
        print("=" * 33)


brand = input("Enter Car Brand: ")
engine_type = input("Enter Engine Type (Petrol/Diesel/Electric): ")

car = Car(brand, engine_type)

car.drive()


# ----------- Question 3 -----------

class Teacher:

    def __init__(self, name):
        self.name = name

    def show_teacher(self):
        print(f"Teacher: {self.name}")


class Department:

    def __init__(self, department_name, teacher):
        self.department_name = department_name
        self.teacher = teacher

    def show_department(self):
        print("\n========== Department ==========")
        print(f"Department: {self.department_name}")
        self.teacher.show_teacher()


teacher_name = input("Enter Teacher Name: ")
department_name = input("Enter Department Name: ")

teacher = Teacher(teacher_name)

department = Department(department_name, teacher)

department.show_department()


# ----------- Question 4 -----------

class Customer:

    def __init__(self, name):
        self.name = name

    def show_customer(self):
        print(f"Customer: {self.name}")


class Bank:

    def __init__(self, bank_name):
        self.bank_name = bank_name

    def serve_customer(self, customer):
        print("\n========== Bank Details ==========")
        print(f"Bank: {self.bank_name}")
        customer.show_customer()
        print("Account Service Completed.")
        print("=" * 32)


customer_name = input("Enter Customer Name: ")
bank_name = input("Enter Bank Name: ")

customer = Customer(customer_name)
bank = Bank(bank_name)

bank.serve_customer(customer)