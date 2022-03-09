def palindrome(st):
    st = list(st)

    if st[0:] == st[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(palindrome("abba"))
