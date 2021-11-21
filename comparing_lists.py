def listCompare(list_1, list_2):
    len1 = len(list_1)
    len2 = len(list_2)
    match_count = 0
    if len1 > len2:
        length = len2
        total = len1
    else:
        length = len1
        total = len2
    for index in range(length):
        try:
            if list_1[index].lower() == list_2[index].lower():
                match_count += 1
        except AttributeError:
            if list_1[index] == list_2[index]:
                match_count += 1
    return round(match_count / total * 100, 1)


list1 = [1, 2.0, 3, "Fred"]
list2 = [1, 2, 3, "fred"]
match1 = listCompare(list1, list2)
print(f"list1 = {list1}\nlist2 = {list2}\n"
      f"match = {match1}%")
print()

list3 = [1, 2, "3", 3, 4, 5, 6, 5, 6, 7]
match2 = listCompare(list2, list3)
print(f"list2 = {list2}\nlist2 = {list3}\n"
      f"match = {match2}%")
