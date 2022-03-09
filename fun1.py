

def capital_indexes(st):
    letters = list(st)
    lst = [i[0] for i in enumerate(letters) if i[1].isupper()]
    return lst


if __name__ == "__main__":
    stl = capital_indexes('HeLLo')
