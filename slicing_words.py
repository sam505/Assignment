def wordPrinter(word, start_index, end_index):
    sliced_word = ""
    if start_index < 0 or end_index >= len(word):
        print("Either the start_index is too small or the stop_index is too large")
    else:
        for i in range(end_index, start_index - 1, -1):
            sliced_word = word[i] + sliced_word
            print(sliced_word)


wordPrinter("incredible", 2, 9)

wordPrinter("disingenuous", 8, 10)

wordPrinter("academic", 0, 7)

wordPrinter("academic", 0, 10)
