def comprehensions(a, b):
    a_list = [a**n for n in range(b+1)]
    print("Te average of list", a_list, end="")
    print(" is ", sum(a_list)/len(a_list), ".", sep="")


comprehensions(6, 3)

# A generator can be used because it generates the nct number in a sequence instead of a list as in list comprehensions
# It returns a generator object rather than a list stored in memory
