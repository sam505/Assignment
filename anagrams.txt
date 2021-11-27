def anagramCheck(word1, word2):
    status = False
    word1_dict = {}
    word2_dict = {}
    for letter in word1:
        try:
            word1_dict[letter] += 1
        except KeyError:
            word1_dict[letter] = 1

    for letter in word2:
        try:
            word2_dict[letter] += 1
        except KeyError:
            word2_dict[letter] = 1
    for key in word1_dict.keys():
        if key not in word2_dict.keys():
            print(f"The words {word1} and {word2} are not anagrams.")
            return False
    if word1 == word2:
        print(f"The words {word1} and {word2} are identical and cannot be anagrams.")
        return False
    else:
        print(f"The words {word1} and {word2} are anagrams ")
        return True


def main():
    word1 = "dad"
    word2 = "add"
    word3 = "odd"
    anagramCheck(word1, word2)
    anagramCheck(word1, word3)
    anagramCheck(word1, word1)


if __name__ == "__main__":
    main()


