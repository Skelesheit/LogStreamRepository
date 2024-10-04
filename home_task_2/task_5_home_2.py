set1 = {6, 31, 14, 25, 19, 3, 55}
set2 = {30, 22, 6, 79, 25}
set3 = {9, 1, 22, 19, 30}


def some_function(set1, set2):
    double_set = set()
    not_included_items = list()
    for item_1, item_2 in zip(set1, set2):
        len_1 = len(double_set)
        len_2 = len(double_set)
        double_set.add(item_1)
        if len_1 == len(double_set):
            not_included_items.append(item_1)
        double_set.add(item_2)
        if len_2 == len(double_set):
            not_included_items.append(item_2)
    return double_set, not_included_items


def join_sets(set1, set2, set3) -> (set, list):
    double_set, not_included_items_1 = some_function(set1, set2)
    print(not_included_items_1)
    final_set, not_included_items_2 = some_function(double_set, set3)
    print(not_included_items_2)
    return final_set, not_included_items_1 + not_included_items_2


def main():
    print("множество 1:", set1)
    print("множество 2:", set2)
    print("множество 3:", set3)

    new_set, not_included_items = join_sets(set1, set2, set3)
    print("Итоговое множество:", new_set)
    print("Невошедшие элементы:", not_included_items)


main()
