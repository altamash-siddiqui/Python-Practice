# Normal Method

numbers = []

for i in range(1, 11):
    numbers.append(i * i)

print("Normal Method:", numbers)


# List Comprehension

squares = [i * i for i in range(1, 11)]

print("List Comprehension:", squares)


# Dictionary Comprehension

numbers = [1, 2, 3, 4, 5]

square_dict = {num: num * num for num in numbers}

print("\nDictionary Comprehension:")
print(square_dict)


# Set Comprehension

numbers = [1, 2, 2, 3, 4, 4, 5, 5]

unique_numbers = {num for num in numbers}

print("\nSet Comprehension:")
print(unique_numbers)


# Generator Expression

numbers = (num * num for num in range(1, 6))

print("\nGenerator Expression:")

for value in numbers:
    print(value)