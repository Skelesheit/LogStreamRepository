from typing import Dict


def get_dict_from_stroke(word: str) -> Dict[str, int]:
    # немного обработаем от возможных неккоретных случаев
    word = word.lower().replace(' ', '').strip()
    letters_in_word: Dict[str, int] = {}
    for letter in set(word):
        letters_in_word[letter] = word.count(letter)
    return letters_in_word


def main():
    line = input('Введите строчку:')
    letters_dict = get_dict_from_stroke(line)
    print("Итоговый результат:")
    print(letters_dict)


main()
