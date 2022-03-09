def div_3(number):

    number = int(number)

    if number % 3 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(div_3(10))
