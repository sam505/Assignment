import numpy as np
import random

array1 = np.array([[random.randint(0, 20) for i in range(4)] for i in range(3)])
array2 = np.array([[random.randint(0, 20) for i in range(4)] for i in range(3)])

print("\nArray 1:\n", array1)
print("\nArray 2:\n", array2)

print("\nCompare arrays using <\n", array1 < array2)

print("\nCompare first row using ==\n", array1[0] == array2[0])

print(f"\nShape of array1: {array1.shape}")

print("\nCompare last column using >\n", array1[:, 3] > array2[:, 3])

print("\nReshape array1 to 2x6\n", array1.reshape(2, 6))

print("\nReshape array2 to 6x2\n", array2.reshape(6, 2))
