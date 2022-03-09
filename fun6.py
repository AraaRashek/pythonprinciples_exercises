
def double_letters(letters):
    for letter in range(len(letters)-1):
        if letters[letter] == letters[letter+1]:
            return True
    return False




if __name__ == "__main__":
    double_letters('nono')
