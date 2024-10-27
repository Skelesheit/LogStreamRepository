import sys
import unittest


def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result


class TestFactorial(unittest.TestCase):
    def test_with_one(self):
        self.assertEqual(factorial(1), 1)

    def test_with_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_with_normal_numbers(self):
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(10), 3628800)

    def test_with_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            factorial(-1)
        self.assertEqual(str(context.exception), "Факториал отрицательного числа не определен")

        with self.assertRaises(ValueError) as context:
            factorial(-2)
        self.assertEqual(str(context.exception), "Факториал отрицательного числа не определен")

        with self.assertRaises(ValueError) as context:
            factorial(-1000)
        self.assertEqual(str(context.exception), "Факториал отрицательного числа не определен")

    def test_with_large_number(self):
        n = 1000
        with self.assertRaises(ValueError) as context:
            factorial(n)
        self.assertIn("не поддерживается типом int", str(context.exception))

    def test_with_float_number(self):
        m = 100.1
        with self.assertRaises(TypeError):
            factorial(m)
