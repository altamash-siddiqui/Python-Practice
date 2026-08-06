# Normal Function

def square(num):
    return num * num


# Lambda Function

square_lambda = lambda num: num * num


number = int(input("Enter a number: "))

print("\nUsing Normal Function:", square(number))
print("Using Lambda Function:", square_lambda(number))


# map() Example

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("\nOriginal List:", numbers)
print("Squared List:", squares)


# filter() Example

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("\nOriginal List:", numbers)
print("Even Numbers:", even_numbers)


# sorted() with Lambda

students = [
    ("Rahul", 82),
    ("Aman", 95),
    ("Sami", 88),
    ("Priya", 76)
]

sorted_students = sorted(students, key=lambda student: student[1])

print("\nStudents Sorted by Marks:")

for student in sorted_students:
    print(student)