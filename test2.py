import time
from concurrent.futures import ThreadPoolExecutor
import math

def cpu_task(n):
    count = 0
    for i in range(1, n):
        count += math.sqrt(i)
    return count

start = time.time()

with ThreadPoolExecutor() as executor:
    results = list(executor.map(cpu_task, [10**6]*8))  # Adjust based on core count

end = time.time()
print(f"Multithreaded CPU workload took {end - start:.2f} seconds")
