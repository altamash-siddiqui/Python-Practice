# Day 25: Functions Practice

def calculate_total(a, b):
    return a + b


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


numbers = [10, 20, 30, 40, 50]

total = calculate_total(10, 20)
average = calculate_average(numbers)

print("========== Day 25 ==========")
print("Total:", total)
print("Average:", average)