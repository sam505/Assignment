import random
import sys

sys.setrecursionlimit(100000)


def createSet(set_size, max_num):
    my_set = set()
    for i in range(set_size):
        my_set.add(random.randint(0, max_num))

    return my_set


inter_count = 0


def intersectionSize(target_size, set_size, max_num):
    global inter_count
    set1 = createSet(set_size, max_num)
    set2 = createSet(set_size, max_num)
    intersection = set1.intersection(set2)
    if len(intersection) >= target_size:
        print(f"Intersection: {intersection}")
        return inter_count
    else:
        inter_count += 1
        return intersectionSize(target_size, set_size, max_num)


target_size = 10
set_size = 20
max_int = 100

count1 = intersectionSize(target_size, set_size, max_int)
count2 = intersectionSize(target_size, set_size, max_int)
count3 = intersectionSize(target_size, set_size, max_int)
count4 = intersectionSize(target_size, set_size, max_int)
count5 = intersectionSize(target_size, set_size, max_int)

print(f"Average iterations needed to get an intersection of {target_size}: ",
      sum([count1, count2, count3, count4, count5]) / 5)

# After increasing the value to 11 or 12 the average number of iterations needed to get an intersection of the
# size required also increases
