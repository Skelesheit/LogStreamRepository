dictionary = {
    "Имя": ["Андрей", "Кирилл", "Анна", "Евгений", "Евгений", "Александр", "Татьяна", "Аркадий", "Игорь", "Кирилл"],
    "Фамилия": ["Иванов", "Лазарев", "Петрова", "Надобников", "Никитин", "Иванов", "Никитина", "Лихачев", "Никитин",
                "Левашев"],
    "Город проживания": ["Москва", "Омск", "Псков", "Псков", "Москва", "Псков", "Москва", "Омск", "Псков", "Москва"],
    "Год рождения": [2000, 1987, 2003, 1993, 2001, 2001, 1976, 1957, 1969, 1999],
    "Месяц рождения": [6, 4, 11, 12, 9, 9, 5, 2, 3, 6],
    "Число рождения": [11, 25, 5, 3, 27, 31, 13, 12, 28, 24],
    "Статус": ["Студент", "Работает", "Школьница", "Работает", "Студент", "Студент", "Работает", "Пенсия", "Работает",
               "Студент"]
}


def remake_dict():
    names = dictionary["Имя"]
    surnames = dictionary["Фамилия"]
    cities = dictionary["Город проживания"]
    statuses = dictionary["Статус"]
    date_year = dictionary["Год рождения"]
    date_month = dictionary["Месяц рождения"]
    date_day = dictionary["Число рождения"]

    fullnames = list()
    new_cities = list()
    new_statuses = list()
    date_list = list()

    for i in range(len(dictionary["Имя"])):
        if surnames[i] == 'Лихачёв' and names[i] == 'Аркадий':
            continue
        if names[i] == 'Кирилл':
            fullnames.append(names[i] + 'л' + '--' + surnames[i])
        else:
            fullnames.append(names[i] + '--' + surnames[i])

        date_list.append((date_year[i], date_month[i], date_day[i]))

        if surnames[i] == 'Иванов' and names[i] == 'Александр':
            new_statuses.append('Работает')
        else:
            new_statuses.append(statuses[i])

        if surnames[i] in 'Никитин':
            new_cities.append('Махачкала')
        else:
            new_cities.append(cities[i])

    new_dict = {
        'Фамилия Имя': fullnames,
        'Дата рождения': date_list,
        'Город проживания': new_cities,
        'Статус': new_statuses
    }
    return new_dict


def update_dict():
    new_dict = remake_dict()
    return new_dict


def main():
    print("Словарь тогда: ", dictionary)
    new_dict = update_dict()
    print("Обновлённый словарь: ")
    for item in new_dict:
        print(item, ": ", new_dict[item])


main()
