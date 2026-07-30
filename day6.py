# ---------- Question 1 ----------

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)


# ---------- Question 2 ----------

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])


# ---------- Question 3 ----------

fruits[1] = "Grapes"

print(fruits)


# ---------- Question 4 ----------

fruits.append("Pineapple")

print(fruits)


# ---------- Question 5 ----------

fruits.remove("Mango")

print(fruits)


# ---------- Question 6 ----------

print("Total Fruits =", len(fruits))


# ---------- Question 7 ----------

for fruit in fruits:
    print(fruit)


# ---------- Question 8 ----------

languages = []

for i in range(5):
    language = input("Enter a programming language: ")
    languages.append(language)

print("\nYour Favorite Programming Languages:")

for language in languages:
    print(language)
    
    
# ---------- Question 9 ----------

fruits = []

for i in range(3):
    fruit = input("Enter a fruit name: ")
    fruits.append(fruit)
    
print("\nYour Favorite Fruits:")

for fruit in fruits:
    print(fruit)
    
    
# ---------- Question 10 ----------

fruits = ["Apple", "Banana", "Mango", "Orange"]

fruit = input("Enter a fruit to search: ")

if fruit in fruits:
    print(fruit, "is available in the list.")
else:
    print(fruit, "is not available in the list.")
    
    
# ---------- Question 11 ----------

numbers = [45, 12, 89, 5, 23]

numbers.sort()

print(numbers)


# ---------- Question 12 ----------

numbers.reverse()

print(numbers)


#--------- Question 13 ----------

marks = [85, 92, 78, 90, 88]
print("Highest marks:", max(marks))

print("Lowest marks:", min(marks))

print("Total marks:", sum(marks))


# ---------- Question 14 ----------

colors = ["Red", "Blue", "Red", "Green", "Red"]

print(colors.count("Red"))


# ---------- Question 15 ----------

fruits = ["Apple", "Banana", "Orange"]

fruits.insert(1, "Mango")

print(fruits)


# ---------- Question 16 ----------

fruits.pop()

print(fruits)


# ---------- Question 17 ----------

students = ["Ali", "Ahmed", "Ayesha"]

students.append("Sara")

students.remove("Ali")

total_students = len(students)

print("Total students:", total_students)

for student in students:

    print(student)
    
    
# ---------- Question 18 ----------

student = {
    "name": "Sami",
    "age": 20,
    "course": "BCA"
}

print(student)
print(student["name"])
print(student["course"])







