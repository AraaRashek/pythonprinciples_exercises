


def up_down(num):
    lower = num-1
    higher = num+1

    new_num = [lower, higher]
    new_num = tuple(new_num)
    return new_num


if __name__ == "__main__":
    print(up_down(5))
