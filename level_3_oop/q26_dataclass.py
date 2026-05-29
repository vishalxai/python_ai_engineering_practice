# Q26 — OOP: Dataclasses
# Rewrite this as a dataclass:
#
# class Product:
#     def __init__(self, name, price, in_stock=True):
#         self.name = name
#         self.price = price
#         self.in_stock = in_stock
#
# Use @dataclass decorator. Add a method: discount(percent) that returns the discounted price.
# Note: dataclass auto-generates __init__, __str__, __repr__ for free.
#
# from dataclasses import dataclass
