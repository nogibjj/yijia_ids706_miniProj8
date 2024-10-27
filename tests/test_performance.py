# import time
# import random
# import psutil
# from stats import mean, median

# process = psutil.Process()

# def get_memory_usage():
#     """Returns the memory usage in MB."""
#     return process.memory_info().rss / 1024 ** 2  # Convert bytes to MB

# def test_mean_performance():
#     numbers = [random.random() for _ in range(10_000_000)]  # Use 10 million elements

#     # Measure initial memory
#     initial_memory = get_memory_usage()

#     # Start timing
#     start_time = time.time()
#     mean(numbers)
#     duration = time.time() - start_time

#     # Measure final memory
#     final_memory = get_memory_usage()

#     print(f"Time taken for mean calculation: {duration:.6f} seconds")
#     print(f"Initial memory usage: {initial_memory:.2f} MB")
#     print(f"Final memory usage: {final_memory:.2f} MB")
#     print(f"Memory consumed by mean calculation: {final_memory - initial_memory:.2f} MB")

# def test_median_performance():
#     numbers = [random.random() for _ in range(10_000_000)]  # Use 10 million elements

#     # Measure initial memory
#     initial_memory = get_memory_usage()

#     # Start timing
#     start_time = time.time()
#     median(numbers)
#     duration = time.time() - start_time

#     # Measure final memory
#     final_memory = get_memory_usage()

#     print(f"Time taken for median calculation: {duration:.6f} seconds")
#     print(f"Initial memory usage: {initial_memory:.2f} MB")
#     print(f"Final memory usage: {final_memory:.2f} MB")
#     print(f"Memory consumed by median calculation: {final_memory - initial_memory:.2f} MB")

# if __name__ == "__main__":
#     test_mean_performance()
#     test_median_performance()
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

    # Collect the performance results as formatted strings
    mean_report = (
        f"### Mean Calculation Performance\n\n"
        f"- Time taken: {duration:.6f} seconds\n"
        f"- Initial memory usage: {initial_memory:.2f} MB\n"
        f"- Final memory usage: {final_memory:.2f} MB\n"
        f"- Memory consumed: {final_memory - initial_memory:.2f} MB\n\n"
    )
    return mean_report

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

    # Collect the performance results as formatted strings
    median_report = (
        f"### Median Calculation Performance\n\n"
        f"- Time taken: {duration:.6f} seconds\n"
        f"- Initial memory usage: {initial_memory:.2f} MB\n"
        f"- Final memory usage: {final_memory:.2f} MB\n"
        f"- Memory consumed: {final_memory - initial_memory:.2f} MB\n\n"
    )
    return median_report

if __name__ == "__main__":
    # Run tests and capture output
    mean_report = test_mean_performance()
    median_report = test_median_performance()

    # Write results to a Markdown file
    with open("python_performance.md", "w") as md_file:
        md_file.write("# Python Performance Report\n\n")
        md_file.write(mean_report)
        md_file.write(median_report)

    print("Performance report saved to python_performance.md")
