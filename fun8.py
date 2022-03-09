

def count(letters):
    result = ''
    for char in letters:
        if char == '-':

            result += char

    counter = len(result) + 1
    if counter == 0:
        return 1
    return counter


if __name__ == "__main__":
    print(count('phor'))
