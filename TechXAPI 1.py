import requests

#API
techxapi = 'test.np.scbtechx.io'
aellaapi = 'test.np.aella.techx'
azscbapi = 'test.np.azscb.tech'


#Code
# Defining a class
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius

# Creating objects and calling methods
circle = Circle(5)
print("Circle Area:", circle.area())
print("Circle Circumference:", circle.circumference())

# Conditional statements
number = random.randint(1, 100)
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# Loops
for i in range(1, 6):
    print(i)

names = ["Alice", "Bob", "Charlie"]
for name in names:
    print("Hello,", name)

# Exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")

# File operations
with open("sample.txt", "w") as file:
    file.write("Hello, World!")

with open("sample.txt", "r") as file:
    contents = file.read()
    print("File Contents:", contents)

# Function with default arguments
def greet(name="Guest"):
    print("Hello,", name)

greet()  # Prints "Hello, Guest"
greet("Alice")  # Prints "Hello, Alice"

# Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# List comprehension
numbers = [1, 2, 3, 4, 5]
squared = [n ** 2 for n in numbers]
print("Squared Numbers:", squared)

# Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print("Person:", person)
print("Name:", person["name"])
print("Keys:", person.keys())
print("Values:", person.values())

# Sets
fruits = {"apple", "banana", "orange"}
fruits.add("grape")
fruits.remove("banana")
print("Fruits:", fruits)

# Modules and packages
random_number = random.randint(1, 10)
print("Random Number:", random_number)

# String formatting
name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))
print(f"Name: {name}, Age: {age}")

# User input
user_input = input("Enter your name: ")
print("Hello,", user_input)
