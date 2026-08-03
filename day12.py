class Student:

    def __init__(self):
        self.name = ""
        self.course = ""

    def set_details(self, name, course):
        self.name = name
        self.course = course

    def show_details(self):
        print("\n===== Student Details =====")
        print("Name   :", self.name)
        print("Course :", self.course)

    def save_details(self):
        with open("student_data.txt", "a") as file:
            file.write(f"Name: {self.name}, Course: {self.course}\n")

        print("\n✅ Student data saved successfully!")

    def show_menu(self):

        print("\n===== MENU =====")
        print("1. Show Details")
        print("2. Save Details")
        print("3. Exit")

        return input("Enter your choice: ")


def get_name():

    while True:

        name = input("Enter Student Name: ")

        if name.replace(" ", "").isalpha():
            return name

        print("❌ Invalid Name! Please enter only alphabets.")


student = Student()

name = get_name()

course = input("Enter Course: ")

student.set_details(name, course)

while True:

    choice = student.show_menu()

    if choice == "1":
        student.show_details()

    elif choice == "2":
        student.save_details()

    elif choice == "3":
        print("\nThank You!")
        break

    else:
        print("\n❌ Invalid Choice!")