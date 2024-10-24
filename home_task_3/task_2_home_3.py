def multi_list(array: list, multi_number=2) -> list:
    return [item * multi_number for item in array]


multi_l = lambda array, multi_number=2: [item * multi_number for item in array]


def main():
    print(multi_list([1, 2, 3, 4, 5], 3))


main()
