from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"function name: {func.__name__}")
        print(f"arguments: {args}")
        result = func(*args, **kwargs)
        print(f"result: {result}")
        return result
    return wrapper


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                raise ValueError("cannot perform sq root of negative numbers")
        result = func(*args, **kwargs)  # called once, after all args pass
        return result
    return wrapper

@logger
@validate_positive
def square_root(n):
    return n ** 0.5

print(square_root(9))
# print(square_root(-4))