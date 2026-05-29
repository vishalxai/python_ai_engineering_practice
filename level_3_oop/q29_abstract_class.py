# Q29 — OOP: Abstract Base Class
# Create an abstract class Shape with:
#   - abstract method area() → must be implemented by subclasses
#   - abstract method perimeter()
#   - concrete method describe() → prints "I am a {classname} with area {area:.2f}"
#
# Implement two subclasses:
#   - Circle(radius)         → area = π * r², perimeter = 2πr
#   - Rectangle(width, height) → area = w * h, perimeter = 2(w + h)
#
# from abc import ABC, abstractmethod
# import math
