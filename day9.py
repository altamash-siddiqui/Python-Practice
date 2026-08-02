# ---------- Question 1 ----------

file = open("notes.txt", "w")

file.write("Hello, Python!\n")
file.write("Welcome to File Handling.")

file.close()

print("Data written successfully.")


# ---------- Question 2 ----------

file = open("notes.txt", "r")

content = file.read()

print(content)

file.close()


# ---------- Question 3 ----------

file = open("notes.txt", "a")

file.write("\nThis is my third line.")

file.close()

print("New data added successfully.")


# ---------- Question 4 ----------

file = open("notes.txt", "r")

line1 = file.readline()
line2 = file.readline()

print("First Line:", line1)
print("Second Line:", line2)

file.close()


# ---------- Question 5 ----------

file = open("notes.txt", "r")

lines = file.readlines()

print(lines)

file.close()