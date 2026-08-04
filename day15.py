class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter Methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter Methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("❌ Invalid Age!")

    def show_details(self):
        print("\n===== Student Details =====")
        print("Name:", self.__name)
        print("Age :", self.__age)


student = Student("Anwar", 20)

print("Before Update:")
student.show_details()

student.set_name("Sami")
student.set_age(21)

print("\nAfter Update:")
student.show_details()