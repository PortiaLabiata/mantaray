from functools import wraps

def null_dec(func):
    return func

def plus_one(func):
    @wraps(func)
    def wrapper(x):
        y = func(x)
        return y + 1
    return wrapper

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE calling {func.__name__}() with args: {args}, kwargs: {kwargs}')
        return func(*args, **kwargs)
    return wrapper

@null_dec
def func():
    print('Hello, world!')

@plus_one
def add_one(x):
    return x+1

@trace
def fuck(name, times=1):
    print(f'Fuck you, {name} {times} times')

fuck('Danya', times=1000000)
