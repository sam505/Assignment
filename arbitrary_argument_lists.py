global avg_int, avg_float


def numbers(*nums):
    ints_count = 0
    floats_count = 0
    ints_sum = 0
    floats_sum = 0
    if len(nums) == 0:
        print(f"There were no values in the list")
        return 0
    else:
        for num in nums:
            if isinstance(num, int):
                ints_count += 1
                ints_sum += num
            elif isinstance(num, float):
                floats_count += 1
                floats_sum += num

    if ints_count != 0 and floats_count != 0:
        print(
            f"The list contained a mix of ints and floats. The average of the ints was {ints_sum / ints_count}, and the "
            f"average of the floats was {floats_sum / floats_count}")
    elif ints_count != 0 and floats_count == 0:
        print(f"The list contained ints, and the average is {ints_sum / ints_count}")
        return 1
    elif ints_count == 0 and floats_count != 0:
        print(f"The list contained floats, and the average is {floats_sum / floats_count}")


print("Mix")
print("Returned: ", numbers(9, 9.0, 4, 65, 100.123))
print("\nEmpty")
print("Returned: ", numbers())
print("\nInts")
print("Returned: ", numbers(1, 2, 3, 4, 5, 6, 7, 8, 9))
print("\nFloats")
print("Returned: ", numbers(1.0, 2.0, 3.0, 4.0, 5.0))
