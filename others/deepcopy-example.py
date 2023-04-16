import numpy as np
import copy

# Create a NumPy array
a = np.array([[1, 2], [3, 4]])

# Create a shallow copy of the array using np.copy()
b = np.copy(a)

# Create a deep copy of the array using deepcopy()
c = copy.deepcopy(a)

# Modify the first element of the original array
a[0] = 5

# Modify the nested list in the original array
a[1][0] = 6

# The shallow copy is affected by the modification to the original array
# print(a[1][0])
print(a)

print(b)   # [1, 2, [6, 4]]

# The deep copy is not affected by the modification to the original array
print(c)   # [1, 2, [3, 4]]