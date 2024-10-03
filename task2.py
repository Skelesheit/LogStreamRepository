def get_number(line: str):
    if line.isdigit():
        return int(line)
    return f"Warning: the '{line}' is not a number"


def get_range_numbers(number: int):
    positive_sum = 0
    negative_sum = 0
    print('array:', end=' ')
    for i in range(-number, number + 1):
        print(i, end=', ')
        if i < 0:
            negative_sum += i
        else:
            positive_sum += i
    print('\n')
    print('positive_sum:', positive_sum)
    print('negative_sum:', negative_sum)


def main():
    print("Welcome to task 2! Write your numbers: ")
    line = get_number(input())
    if isinstance(line, int):
        get_range_numbers(line)
    else:
        print(f"Warning: the '{line}' is not a number")
    print("Thank you for using task 2!")


main()
