def string_formatter(sep, *strings):
    final_string = ""
    for string in strings:
        final_string = final_string + str(string)
        if strings.index(string) != len(strings)-1:
            final_string = final_string + sep

    return final_string


print(string_formatter("-", "these", "are", "some", "strings"))
print(string_formatter("_@_", "these", "are", "some", "strings"))
print(string_formatter("-", "this", "is", "a", "test", "of", "some", "strings"))
print(string_formatter("_@_", "this", "is", "a", "test", "of", "some", "strings"))
