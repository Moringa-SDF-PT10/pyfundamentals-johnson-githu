# Task 1: Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2


# Task 2: Function to check if a number is even
def is_even(number):
    return number % 2 == 0


# Task 3: Function to reverse a string
def reverse_string(text):
    return text[::-1]


# Task 4: Function to count vowels in a string (case-insensitive)
def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)


# Task 5: Function to calculate factorial of a non-negative integer
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


# Task 6: Decorator and function to apply the decorator
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

# Function to apply the decorator to another function
def apply_decorator(func):
    return decorator_func(func)


# Task 7: Function to sort a list of (name, age) tuples by age
def sort_by_age(people):
    return people[::-1]


# Task 8: Function to merge two dictionaries and sum values of common keys
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged


# Task 9: Class representing a Car with display functionality
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Test block (only runs when this file is executed directly)
if __name__ == "__main__":
    print("\n=== Running Tasks ===")
    
    # Comment/uncomment these lines to test specific functions
    print("add_numbers(3, 4):", add_numbers(3, 4))
    print("is_even(10):", is_even(10))
    print("reverse_string('hello'):", reverse_string("hello"))
    print("count_vowels('Johnson Githu'):", count_vowels("Johnson Githu"))
    print("calculate_factorial(5):", calculate_factorial(5))

    @apply_decorator
    def greet():
        print("Hello!")

    greet()

    people = [("Alice", 30), ("Johnson", 25), ("Ken", 35)]
    print("sort_by_age:", sort_by_age(people))

    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    print("merge_dicts:", merge_dicts(dict1, dict2))

    car = Car("Mercedes", "G Wagon", 2022)
    print("Running after initializing Car Info:")
    car.display_info()