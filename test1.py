import numpy as np
import time

size = 300000  # Adjust based on system capability

A = np.random.rand(size, size)
B = np.random.rand(size, size)

start = time.time()
C = np.dot(A, B)
end = time.time()

print(f"Matrix multiplication took {end - start:.2f} seconds")