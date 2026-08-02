# ---------- Question 1 ----------

class Student:

    def welcome(self):
        print("Welcome to Python OOP!")

student1 = Student()

student1.welcome()


# ---------- Question 2 ----------

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_details(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


student1 = Student("Sami", 20, "BCA")

student1.show_details()


# ---------- Question 3 ----------

student2 = Student("Ali", 21, "BCA")
student3 = Student("Ayesha", 19, "B.Tech")

student2.show_details()
student3.show_details()


# ---------- Question 4 ----------

name = input("\nEnter Student Name: ")
age = int(input("Enter Student Age: "))
course = input("Enter Student Course: ")

student4 = Student(name, age, course)

print("\nStudent Entered By User")
student4.show_details()