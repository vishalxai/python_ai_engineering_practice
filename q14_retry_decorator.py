# Q14 — Level 3: Functions and Real Patterns
# Write a function: retry(func, max_attempts=3)
# It calls func(). If it raises an exception, it retries — up to max_attempts times total.
# If all attempts fail, raise the last exception.
# If it succeeds, return the result.
#
# Bonus: add a print/log message on each retry so you can see it working.
## a decorator is just a function that wraps another function 
# *args and **kwargs let the wrapper accept any function's arguments without knowing them in advance 

def retry(func):
    def wrapper(*args,**kwargs):
        for attempt in range(3):
            try:
                return func(*args,**kwargs)
            except Exception as e:
                last_error = e 
                print(f"Attempt {attempt + 1} failed: {e}")
        raise last_error

    return wrapper

@retry
def unstable():
    import random
    if random.random()<0.7:
        raise ValueError("something went wrong")
    return "success"
print(unstable())

