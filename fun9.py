def is_anagram(word1, word2):
    word1 = list(sorted(word1))
    word2 = list(sorted(word2))

    if word1 == word2:
        return True
    return False


if __name__ == "__main__":
    print(is_anagram("typhoon", "opython"))
