class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"\nHello, my name is {self.name}.")


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    # Method Overriding
    def introduce(self):
        print(f"\nHello, my name is {self.name}.")
        print(f"I am studying {self.course}.")

    def show_course(self):
        print(f"Course: {self.course}")


name = input("Enter Student Name: ")
course = input("Enter Course: ")

student = Student(name, course)

student.introduce()
student.show_course()