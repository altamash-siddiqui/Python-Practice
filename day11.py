# ---------- Question 1 ----------

student = {
    "name": "Anwar",
    "course": "BCA",
    "language": "Python"
}

print(student)
print(student["name"])
print(student["course"])
print(student["language"])


# ---------- Question 2 ----------

student = {
    "name": "Altamash",
    "course": "BCA",
    "language": "Python"
}

print("Original Dictionary:")
print(student)

# Add a new key
student["college"] = "Integral University"

# Update existing value
student["language"] = "Python & AI"

print("\nUpdated Dictionary:")
print(student)

print("\nStudent Details:")
for key, value in student.items():
    print(f"{key} : {value}")
    
    
# ---------- Question 3 ----------

student = {
    "name": "Anwar",
    "course": "BCA",
    "language": "Python"
}

print("Student Dictionary:")
print(student)

print("\nKeys:")
for key in student.keys():
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in student.items():
    print(f"{key} : {value}")

print("\nChecking if 'course' exists:")
print("course" in student)

print("\nChecking if 'age' exists:")
print("age" in student)