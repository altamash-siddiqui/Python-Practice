# *args Example

def add_numbers(*numbers):

    total = 0

    for num in numbers:
        total += num

    return total


print(add_numbers(10, 20))
print(add_numbers(1, 2, 3, 4, 5))
print(add_numbers(100, 200, 300, 400))


# **kwargs Example

def student_details(**details):

    print("\nStudent Details:")

    for key, value in details.items():
        print(f"{key}: {value}")


student_details(
    name="Altamash",
    age=20,
    course="BCA",
    city="Kanpur"
)


# Decorator Example

def my_decorator(function):

    def wrapper():

        print("\nBefore Function Execution")

        function()

        print("After Function Execution")

    return wrapper


@my_decorator
def greet():

    print("Hello Altamash! Welcome to Python.")


greet()


# Decorator with *args and **kwargs

def my_decorator(function):

    def wrapper(*args, **kwargs):

        print("\n===== Before Function =====")

        result = function(*args, **kwargs)

        print("===== After Function =====")

        return result

    return wrapper


@my_decorator
def add(a, b):

    print(f"Sum = {a + b}")


@my_decorator
def introduce(name, course):

    print(f"My name is {name}")
    print(f"Course: {course}")


add(10, 20)

introduce(name="Altamash", course="BCA")