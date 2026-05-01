import datetime
from utils import greet, add, subtract, multiply, divide 

print("Name: Pelob Chakraborti")
print("Today's date:", datetime.date.today())

print("Addition:", add(5, 3))
print("Subtraction:", subtract(5, 3))
print("Multiply:", multiply(3, 4))
print("Division:", divide(10, 2))
print("Division by zero:", divide(10, 0))