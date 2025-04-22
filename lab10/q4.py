import numpy as np

N = int(input())
cartesian = np.random.rand(N, 2) * 100

x = cartesian[:, 0]
y = cartesian[:, 1]

r = np.sqrt(x**2 + y**2)   
theta = np.arctan2(y, x)  

polar = np.column_stack((r, theta))

print("Cartesian Coordinates:\n", cartesian)
print("\nPolar Coordinates:\n", polar)
