# Lambda Function Example

square = lambda x: x * x

print(square(5))
print(square(10))


# map() with Lambda

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print("\nOriginal List:")
print(numbers)

print("\nSquared List:")
print(squares)


# filter() with Lambda

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("\nOriginal List:")
print(numbers)

print("\nEven Numbers:")
print(even_numbers)


# sorted() with Lambda

students = [
    ("Sami", 85),
    ("Rahul", 92),
    ("Aman", 78),
    ("Zaid", 95)
]

sorted_students = sorted(
    students,
    key=lambda student: student[1]
)

print("\nStudents Sorted by Marks:")

for student in sorted_students:
    print(student)
    
    
sorted_students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("\nStudents Sorted (Highest Marks First):")

for student in sorted_students:
    print(student)