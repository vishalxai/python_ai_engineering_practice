# Q43 — Production: Environment Variables
# In real AI apps, API keys and config NEVER go in code — they go in .env files.
#
# 1. Write a function get_config() that reads these from environment variables:
#    - OPENAI_API_KEY (required — raise ValueError if missing)
#    - APP_ENV (optional — default to "development")
#    - MAX_TOKENS (optional — default to 1000, return as int)
#
# 2. Create a sample .env file (add it to .gitignore!)
#
# import os
# from dotenv import load_dotenv  ← pip install python-dotenv
#
# load_dotenv() loads the .env file into os.environ automatically.
