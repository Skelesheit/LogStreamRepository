def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)


if __name__ == '__main__':
    # сначала на корректные данные
    assert average_num([1, 2, 3, 4]) == 2.5
    assert average_num([1]) == 1
    assert average_num([1.5, 2.5, 3.5]) == 2.5
    assert average_num([0, 0, 0]) == 0.0
    assert average_num([100, 100000.01, 0]) == 33366.67
    assert average_num([-1, -2, -3, -4]) == -2.5
    # теперь неккоректные данные
    assert average_num(['5', '10', 15]) == 10.0
    assert average_num(['a', 'b', 'c']) == "Bad request"
    assert average_num([None, 2, 3]) == "Bad request"
    # False считается за 0? по идее тоже "Bad request"
    assert average_num([False, 2, 3, 4]) == 2.25
    # а если на возможные ошибки?
    try:
        assert average_num([]) == "Bad request"
    except ZeroDivisionError:
        print("ZeroDivisionError")
