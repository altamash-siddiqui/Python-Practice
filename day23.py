# Iterable Example

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)
    
    
# Iterator Example

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

print("\nUsing next():")

print(next(iterator))
print(next(iterator))
print(next(iterator))


# StopIteration Example

numbers = [10, 20]

iterator = iter(numbers)

try:

    while True:

        print(next(iterator))

except StopIteration:

    print("\nIterator Finished!")
    
    
# Custom Iterator

class CountUp:

    def __init__(self, limit):

        self.limit = limit

        self.current = 1

    def __iter__(self):

        return self

    def __next__(self):

        if self.current <= self.limit:

            value = self.current

            self.current += 1

            return value

        else:

            raise StopIteration


counter = CountUp(5)

print("\nCustom Iterator:")

for number in counter:

    print(number)