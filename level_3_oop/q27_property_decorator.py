# Q27 — OOP: @property (getter and setter)
# Create a Temperature class:
#   - Store temperature privately as _celsius
#   - @property celsius → returns _celsius
#   - @celsius.setter   → sets _celsius but raises ValueError if below -273.15 (absolute zero)
#   - @property fahrenheit → returns the celsius value converted to Fahrenheit (formula: C * 9/5 + 32)
#
# Test:
#   t = Temperature(25)
#   print(t.fahrenheit)   → 77.0
#   t.celsius = -300      → raises ValueError
