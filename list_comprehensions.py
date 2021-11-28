def comprehensions(a, b):
    a_list = [a**n for n in range(b+1)]
    print("List: ", a_list)
    print("Average: ", sum(a_list)/len(a_list))


comprehensions(6, 3)

# A generator can be used because it generates the nct number in a sequence instead of a list as in list comprehensions
# It returns a generator object rather than a list stored in memory
