# ---------- Question 1 ----------
for i in range(5):
    print(i)

# ---------- Question 2 ----------
for i in range(1, 6):
    print(i)

# ---------- Question 3 ----------
for i in range(2, 11, 2):
    print(i)

# ---------- Question 4 ----------
for i in range(10, 0, -1):
    print(i)

# ---------- Question 5 ----------
for i in range(1, 20):
    print(i)

# ---------- Question 6 ----------
for i in range(2, 20, 2):
    print(i)

# ---------- Question 7 ----------
for i in range(1, 20, 2):
    print(i)

# ---------- Question 8 ----------
for i in range(7, 78, 7):
    print(i)

# ---------- Question 9 ----------
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)

# ---------- Question 10 ----------
for i in range(1, 11):
    print("8 /", i, "=", 8 / i)

# ---------- Question 11 ----------
for i in range(1, 11):
    print(i * i)

# ---------- Question 12 ----------
total = 0
for i in range(1, 101):
    total += i
print("Sum of first 100 natural numbers:", total)

# ---------- Question 13 ----------
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print("Sum of first 100 even numbers:", total)

# ---------- Question 14 ----------
total = 0
for i in range(1, 101):
    if i % 2 != 0:
        total += i
print("Sum of first 100 odd numbers:", total)

# ---------- Question 15 ----------
count = 0
while count <= 5:
    print(count)
    count += 1

# ---------- Question 16 ----------
number = 10
while number >= 1:
    print(number)
    number -= 1

# ---------- Question 17 ----------
number = 20
while number >= 1:
    print(number)
    number -= 1

# ---------- Question 18 ----------
number = 20
while number >= 1:
    if number % 2 == 0:
        print(number)
    number -= 1

# ---------- Question 19 ----------
number = 100
while number >= 1:
    print(number)
    number -= 1

# ---------- Question 20 ----------
for i in range(1, 11):
    if i == 6:
        break
    print(i)

# ---------- Question 21 ----------
for i in range(1, 11):
    if i == 6:
        continue
    print(i)

# ---------- Question 22 ----------
for i in range(1, 11):
    if i == 6:
        pass
    else:
        print(i)

# ---------- Question 23 ----------
for i in range(1, 51):
    if i % 2 != 0:
        print(i)

# ---------- Question 24 ----------
password = input("Enter your password: ")

while password != "secret":
    print("Incorrect password. Try again.")
    password = input("Enter your password: ")

print("Access granted. Welcome!")

# ---------- Question 25 ----------
for i in range(1, 11):
    if i % 2 != 0:
        print(i, "is odd")