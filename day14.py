class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"\nHello! My name is {self.name}.")


class Student:

    def __init__(self, course):
        self.course = course

    def introduce(self):
        print(f"\nI am studying {self.course}.")


class CollegeStudent(Person, Student):

    def __init__(self, name, course, college):
        Person.__init__(self, name)
        Student.__init__(self, course)
        self.college = college

    def show_college(self):
        print(f"College: {self.college}")


name = input("Enter Name: ")
course = input("Enter Course: ")
college = input("Enter College Name: ")

student = CollegeStudent(name, course, college)

student.introduce()
student.show_college()

print("\nMethod Resolution Order (MRO):")
print(CollegeStudent.__mro__)