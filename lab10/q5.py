import numpy as np

arr = np.array(['apple', 'banana', 'kiwi', 'mango', 'papita'])

centered = np.array([s.center(15, '_') for s in arr])
left = np.array([s.ljust(15, '_') for s in arr])
right = np.array([s.rjust(15, '_') for s in arr])

print("Original:\n", arr)
print("\nCentered:\n", centered)
print("\nLeft-Justified:\n", left)
print("\nRight-Justified:\n", right)
