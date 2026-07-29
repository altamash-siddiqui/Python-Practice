# ---------- Question 1 ----------
def greet():
    print("Hello!")
    print("Welcome to Python Functions.")

greet()


# ---------- Question 2 ----------
def college():
    print("I am learning Python.")
    print("I will become a Software Developer.")

college()


# ---------- Question 3 ----------
def greet(name):
    print("Hello,", name)
    
greet("Sami")


# ---------- Question 4 ----------
def add(a, b):
    print("Sum:", a + b)
    
add(10, 20)


# ---------- Question 5 ----------
def multiply(a, b):
    print("Multiplication:", a * b)
    
multiply(5, 8)


# ---------- Question 6 ----------
def square(number):
    print("Square =", number * number)
    
square(7)


# ---------- Question 7 ----------
def cube(number):
    print("Cube =", number * number * number)
    
cube(3)


# ---------- Question 8 ----------
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum =", result)


# ---------- Question 9 ----------
def square(number):
    return number * number

answer = square(6)

print("Square =", answer)


# ---------- Question 10 ----------
def cube(number):
    return number * number * number

answer = cube(4)
print("Cube =", answer)


# ---------- Question 11 ----------
def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)

print("Sum =", result)


# ---------- Question 12 ----------
def multiply(a, b):
    return a * b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

answer = multiply(x, y)

print("Multiplication =", answer)


# ---------- Question 13 ----------
def substract(a, b):
    return a - b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = substract(x, y)

print("Substraction =", result)


# ---------- Question 14 ----------
def student(name, age):
    print("Name:", name)
    print("Age:", age)
    
student("Altamash", 20)


# ---------- Question 15 ----------
def employee(name, salary):
    print("Name:", name)
    print("Salary:", salary)
    
employee("Ali", 50000)


# ---------- Question 16 ----------
def student(name, age):
    return f"Name: {name}\nAge: {age}"

name = input("Enter your name: ")
age = int(input("Enter your age: "))

result = student(name, age)

print(result)


# ---------- Question 17 ----------
def is_even(number):
    if number % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"
    
num = int(input("Enter a number: "))

print(is_even(num))


# ---------- Question 18 ----------
def largest(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = largest(num1, num2)

print("Largest number is:", result)
