def print_data_person(name: str, surname: str, age: int):
    return 'it is stroke with format(): \n Ваше имя: {name}, Фамилия {surname}, Возраст: {age} '.format(name=name,
                                                                                                        surname=surname,
                                                                                                        age=age)


def print_f_stroke_data_person(name: str, surname: str, age: int):
    return f'it is f-stroke: \n Ваше имя: {name}, Фамилия: {surname}, Возраст: {age}'


def main():
    print(print_data_person('John', 'Smith', 18))
    print()
    print(print_f_stroke_data_person('Марк', 'Смит', 20))


main()
