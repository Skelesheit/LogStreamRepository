import functools

from home_4_task_2 import fibonacci


# важно знать про functools
# иначе теряется подсказка аргументов
def fibonacci_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Функция '{func.__name__}' была вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


# та же декорация, но без синтаксического сахара @
# используется код из файла home_4_task_2
new_fibonacci = fibonacci_log(fibonacci)

print(*new_fibonacci(1000))
