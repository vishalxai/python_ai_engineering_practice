# Q49 — Production: SQLAlchemy (ORM basics)
# Write a complete SQLAlchemy setup with:
#
# 1. A User model (table: users):
#    - id (primary key, autoincrement)
#    - name (string, not null)
#    - email (string, unique, not null)
#    - created_at (datetime, default = now)
#
# 2. Functions:
#    - create_user(name, email) → inserts a new user, returns the user object
#    - get_user_by_email(email) → returns user or None
#    - get_all_users() → returns list of all users
#    - delete_user(user_id) → deletes the user
#
# Use SQLite for simplicity: engine = create_engine("sqlite:///test.db")
#
# from sqlalchemy import create_engine, Column, Integer, String, DateTime
# from sqlalchemy.orm import declarative_base, sessionmaker
