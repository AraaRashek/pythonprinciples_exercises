def zap(a, b):

    c = [(a[i], b[i]) for i in range(len(a))]
    return c


if __name__ == "__main__":
    print(zap(
        [0, 1, 2, 3],
        [5, 6, 7, 8]
    ))
