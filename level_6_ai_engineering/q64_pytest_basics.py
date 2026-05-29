# Q64 — Production: pytest
# Interviews often ask you to write tests. Know the basics cold.
#
# Write pytest tests for this function:
def calculate_discount(price: float, percent: float) -> float:
    if percent < 0 or percent > 100:
        raise ValueError("Percent must be between 0 and 100")
    return price * (1 - percent / 100)

# Write test functions for:
#   1. Normal case: 100 price, 10% discount → 90.0
#   2. Zero discount → price unchanged
#   3. 100% discount → 0.0
#   4. Negative percent → raises ValueError
#   5. Percent > 100 → raises ValueError
#
# Also write tests for the filter_by_key function from Q11.
# (copy it here or import it)
#
# Run with: pytest q64_pytest_basics.py -v
# pip install pytest
