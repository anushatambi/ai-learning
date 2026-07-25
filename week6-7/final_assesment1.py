import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

def retry(max_attempts, delay):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            return "All retries failed"
        return wrapper
    return decorator

@timer
@retry(max_attempts=3, delay=2)
def simulate_api_call(n):
    if n%2==0:
        return 'Success'
    else:
        raise ConnectionError("API unavailable")

simulate_api_call(3)
simulate_api_call(2)