


def get_row_col(st):

    st = st.replace('A', '0')
    st = st.replace('B', '1')
    st = st.replace('C', '2')

    st = map(int, st)
    st = list(st)
    st[1] = st[1]-1
    st[1], st[0] = st[0], st[1]

    st = tuple(st)

    return st


if __name__ == "__main__":
    print(get_row_col("C1"))
