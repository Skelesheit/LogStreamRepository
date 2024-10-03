ship_cells = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"


def is_hit_ships(step: str):
    upper_step = step.upper()
    if upper_step in ship_cells:
        return True
    return False


def main():
    step = input('Введите ход:')
    print('you hit to cell' if is_hit_ships(step) else 'you do not hit to cell')


main()
