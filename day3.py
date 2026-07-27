age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")


temperature = float(input("Enter the temperature: "))

if temperature > 40:
    print("It's a very hot day.")
elif temperature > 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a normal day.")
elif temperature > 10:
    print("It's a cold day.")
else:
    print("It's a very cold day.")