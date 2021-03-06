def words_key_value_pairs(paragraph):
    words_dict = {}
    words = paragraph.split()
    for word in words:
        word = word.lower()
        try:
            words_dict[word] += 1
        except:
            words_dict[word] = 1
    return words_dict


def letters_key_value_pairs(paragraph):
    letters_dict = {}
    words = paragraph.split()
    for word in words:
        word = word.lower()
        for letter in word:
            try:
                letters_dict[letter] += 1
            except:
                letters_dict[letter] = 1
    return letters_dict


paragraph = "People list to see examples of this type of thing working, so using this sentence as an example, " \
            "the outputs would be "

words = words_key_value_pairs(paragraph)
letters = letters_key_value_pairs(paragraph)

sorted_words = sorted(words.items(), key=lambda kv: kv[1], reverse=True)
sorted_letters = sorted(letters.items(), key=lambda kv: kv[1], reverse=True)
for word in sorted_words:
    print("words", word)
print()

for letter in sorted_letters:
    print("letters =", letter)
