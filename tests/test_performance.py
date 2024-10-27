import time
import random
import psutil
from stats import mean, median

process = psutil.Process()

def get_memory_usage():
    """Returns the memory usage in MB."""
    return process.memory_info().rss / 1024 ** 2  # Convert bytes to MB

def test_mean_performance():
    numbers = [random.random() for _ in range(10_000_000)]  # Use 10 million elements

    # Measure initial memory
    initial_memory = get_memory_usage()

    # Start timing
    start_time = time.time()
    mean(numbers)
    duration = time.time() - start_time

    # Measure final memory
    final_memory = get_memory_usage()

    print(f"Time taken for mean calculation: {duration:.6f} seconds")
    print(f"Initial memory usage: {initial_memory:.2f} MB")
    print(f"Final memory usage: {final_memory:.2f} MB")
    print(f"Memory consumed by mean calculation: {final_memory - initial_memory:.2f} MB")

def test_median_performance():
    numbers = [random.random() for _ in range(10_000_000)]  # Use 10 million elements

    # Measure initial memory
    initial_memory = get_memory_usage()

    # Start timing
    start_time = time.time()
    median(numbers)
    duration = time.time() - start_time

    # Measure final memory
    final_memory = get_memory_usage()

    print(f"Time taken for median calculation: {duration:.6f} seconds")
    print(f"Initial memory usage: {initial_memory:.2f} MB")
    print(f"Final memory usage: {final_memory:.2f} MB")
    print(f"Memory consumed by median calculation: {final_memory - initial_memory:.2f} MB")

if __name__ == "__main__":
    test_mean_performance()
    test_median_performance()
