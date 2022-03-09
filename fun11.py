def largest_difference(lst):
    maxi = max(lst)
    mini = min(lst)

    return maxi-mini


if __name__ == "__main__":
    print(largest_difference([1, 2, 3])
          )
