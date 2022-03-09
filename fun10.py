def flatten(lst):
    lst = [x for l in lst for x in l]
    return lst


if __name__ == "__main__":
    print(flatten([[1, 2], [3, 4]]))
