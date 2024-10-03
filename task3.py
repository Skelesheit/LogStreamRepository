from itertools import permutations


def get_three_digit_number(line: str):
    if not line.isdigit():
        return f"'{line}' is not a number"
    if not len(line) == 3:
        return f"{line} is not a three-digit number"
    if not len(set(line)) == 3:
        return f"{line} hasn't 3 unique digits"
    return int(line)


def get_permutation_numbers(number: int):
    digits = [number // 100, (number % 100) // 10, number % 10]
    return [digit[0] * 100 + digit[1] * 10 + digit[2]
            for digit in permutations(digits, 3)]


def main():
    print("Welcome to task 3! Write your numbers: ")
    number = get_three_digit_number(input())
    if isinstance(number, int):
        permutation_numbers = get_permutation_numbers(number)
        print("permutation numbers: ", *permutation_numbers)
    else:
        print(f"Your number is invalid: {number}")
    print("Thank you for using task 3!")


main()
