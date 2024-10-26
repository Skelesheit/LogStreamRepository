def fibonacci(n):
    a, b = 1, 1
    while b <= n:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    for number in fibonacci(1000):
        print(number, end=' ')
