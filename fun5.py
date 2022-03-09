

def only_ints(a, b):

    if type(a) == type(b) == int:
        return True
    return False


if __name__ == "__main__":
    only_ints("a", 1)
