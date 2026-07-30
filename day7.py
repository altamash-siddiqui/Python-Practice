# ---------- Question 1 ----------

student = {
    "name": "Sami",
    "age": 20,
    "course": "BCA"
}

print(student)


# ---------- Question 2 ----------

print(student["name"])
print(student["age"])
print(student["course"])


# ---------- Question 3 ----------

student["college"] = "ABC College"

print(student)


# ---------- Question 4 ----------

student["age"] = 21

print(student)


# ---------- Question 5 ----------

del student["course"]

print(student)


# ---------- Question 6 ----------

for key, value in student.items():
    print(key, ":", value)
    
    
# ---------- Question 7 ----------

if "age" in student:
    print("Age key is available.")
else:
    print("Age key is not available.")
    
    
# ---------- Question 8 ----------

student = {
    "name": "Sami",
    "age": 20,
    "course": "BCA",
    "address": {
        "city": "Mumbai",
        "state": "Maharashtra"
    }
}

print(student["address"]["city"])
print(student["address"]["state"])