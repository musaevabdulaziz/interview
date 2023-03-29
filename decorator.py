import functools


def repeat(_func=None, *, number=2):
    def my_decor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(number):
                value = func(*args, **kwargs)
            return value
        return wrapper
    
    if _func is None:
        return my_decor
    return my_decor(_func)


@repeat()
def say_whee():
    print("Hello world")

@repeat(number=4)
def greet(name):
    print(f"Hello {name}")


print(say_whee())
print(greet("Abdulaziz"))