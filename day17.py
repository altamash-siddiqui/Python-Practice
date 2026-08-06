import json

student = {
    "name": "Altamash",
    "course": "BCA",
    "language": "Python"
}

# Save Data
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("✅ Data Saved Successfully!")

# Read Data
with open("student.json", "r") as file:
    data = json.load(file)

print("\nStudent Details")
print("Name:", data["name"])
print("Course:", data["course"])
print("Language:", data["language"])