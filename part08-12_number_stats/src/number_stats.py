class NumberStats:
    def __init__(self):
        self.numbers = []
        self.even_numbers = []
        self.odd_numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)
        if number % 2 == 0:
            self.even_numbers.append(number)
        else:
            self.odd_numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if len(self.numbers) == 0:
            return 0
        else:
            return sum(self.numbers) / len(self.numbers)

    def get_sum_even(self):
        return sum(self.even_numbers)

    def get_sum_odd(self):
        return sum(self.odd_numbers)


all_numbers = NumberStats()
even_numbers = NumberStats()
odd_numbers = NumberStats()

print("Please type in integer numbers:")
while True:
    number = int(input())
    if number == -1:
        break
    all_numbers.add_number(number)
    if number % 2 == 0:
        even_numbers.add_number(number)
    else:
        odd_numbers.add_number(number)

print("Sum of numbers:", all_numbers.get_sum())
print("Mean of numbers:", all_numbers.average())
print("Sum of even numbers:", even_numbers.get_sum())
print("Sum of odd numbers:", odd_numbers.get_sum())
