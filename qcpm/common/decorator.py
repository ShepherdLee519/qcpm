from functools import wraps

def countDecorator(func):
    index = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal index
        r = func(*args, index = index, **kwargs)
        index += 1

        return r
    return wrapper