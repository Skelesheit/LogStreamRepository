dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}


def get_sets(input_dict: dict[int, int]):
    keys, values = set(), set()
    for key, value in input_dict.items():
        keys.add(key)
        values.add(value)
    return keys, values


def join_sets(set_one: set(), set_two: set()) -> set():
    set_three = set()
    for key, value in zip(set_one, set_two):
        set_three.add(key)
        set_three.add(value)
    return set_three


def main():
    input_dict = dct
    keys, values = get_sets(input_dict)
    answer = join_sets(keys, values)
    print("Итоговое множество: ")
    print(answer)


main()
