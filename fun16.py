

def consecutive_zeros(st):

    return max(map(len, st.split('1')))


if __name__ == "__main__":
    print(consecutive_zeros("1001101000110"))
