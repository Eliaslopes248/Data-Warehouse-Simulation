COLOR_MAP = {
    "yellow"    : 33,
    "green"     : 34,
    "red"       : 31
}


def color_print(txt, color, newLine=True):
    if not txt or len(txt) == 0:
        return
    if color not in COLOR_MAP:
        return
    if not newLine:
        print(f'\033[{COLOR_MAP[color]}m{txt}\033[0m', end=" ")
    print(f'\033[{COLOR_MAP[color]}m{txt}\033[0m')
    