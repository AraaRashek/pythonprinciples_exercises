



def add_dots(letters):

    result = ''

    for letter in letters:
        dot = '.'
        result += letter + dot

    return result[:-1]


def remove_dots(letters):

    letters = letters.replace('.', '')

    return letters


if __name__ == "__main__":
    add_dots("test")
    remove_dots('t.e.s.t')
