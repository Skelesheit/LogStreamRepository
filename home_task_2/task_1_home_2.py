def get_args():
    list_numbers = [int(item) for item in input('Введите список:').split()]
    power_number = int(input('Введите степень:'))
    return list_numbers, power_number


def main():
    list_numbers, power_number = get_args()


main()
