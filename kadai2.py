import numpy  as np

a = np.array([1,2,3,4])
b = np.array([4,3,2,1])
x = np.linalg.norm(a - b)

print(x)