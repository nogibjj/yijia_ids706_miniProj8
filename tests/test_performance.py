import time
from src.stats import mean, median

def test_mean_performance():
    numbers = [1.0] * 1_000_000

    start = time.time()
    mean(numbers)
    duration = time.time() - start
    print(f"Python - Time taken for mean calculation: {duration:.6f} seconds")

def test_median_performance():
    numbers = [1.0] * 1_000_000

    start = time.time()
    median(numbers)
    duration = time.time() - start
    print(f"Python - Time taken for median calculation: {duration:.6f} seconds")

if __name__ == "__main__":
    test_mean_performance()
    test_median_performance()
