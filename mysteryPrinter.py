def mysteryPrinter(list1, list2):
    sum1 = list1[0] + list2[-1]
    sum2 = list1[-1] + list2[0]
    sum3 = sum(list1) - sum(list2)
    sum4 = min(list1) + min(list2)
    sum5 = (sum(list1) / len(list1) - sum(list2) / len(list2))

    if len(list1) > len(list2):
        print("List1 is longer than list2.")
    elif len(list2) > len(list1):
        print("List2 is longer than list1.")
    else:
        print("The two lists are the same length.")

    if len(list1) > 20 or len(list2) > 20:
        print("One of the lists is too long.")
    else:
        print(f"Mystery sum1: {sum1}\n"
              f"Mystery sum2: {sum2}\n"
              f"Mystery sum3: {sum3}\n"
              f"Mystery sum4: {sum4}\n"
              f"Mystery sum5: {sum5}")


print("mysterious")
mysteryPrinter([1, 2, 4, 6, 3], [0, 6, 8, 4])
