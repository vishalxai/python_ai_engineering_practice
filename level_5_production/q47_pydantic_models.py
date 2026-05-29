# Q47 — Production: Pydantic Models
# Pydantic is used everywhere in FastAPI for validation. Practice the key patterns.
#
# 1. Create a UserCreate model:
#    - name: str (min 2 chars)
#    - email: str (must contain @)
#    - age: int (must be >= 0)
#    - role: str (default = "viewer")
#
# 2. Create a nested model: Address with street, city, country
#    Add an optional address field to UserCreate
#
# 3. Create a UserResponse model (same as UserCreate but add id: int)
#    Use model_validator or @computed_field if needed
#
# Test: try creating a user with invalid data and catch the ValidationError
#
# from pydantic import BaseModel, field_validator, ValidationError
