# factorial_recursive.py

import time

# Recursive function to compute factorial of a number
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial(n - 1)
        return n * factorial(n - 1)

# Measure execution time for various input sizes
input_sizes = list(range(1, 21))  # n = 1 to 20
execution_times = []

for n in input_sizes:
    start_time = time.time()
    result = factorial(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    execution_times.append(elapsed_time)
    print(f"n = {n}, factorial = {result}, time = {elapsed_time:.10f} seconds")