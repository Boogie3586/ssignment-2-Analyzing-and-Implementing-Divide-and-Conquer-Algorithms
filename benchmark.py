import time
import random
from merge_sort import merge_sort
from quick_sort import quick_sort

def time_sort(sort_func, data):
    start = time.perf_counter()
    sort_func(data.copy())  # use copy to avoid modifying original data
    end = time.perf_counter()
    return end - start

def generate_data(size=10000):
    sorted_data = list(range(size))
    reverse_data = list(range(size, 0, -1))
    random_data = [random.randint(1, size) for _ in range(size)]
    return sorted_data, reverse_data, random_data

def main():
    sorted_data, reverse_data, random_data = generate_data()

    algorithms = {
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    datasets = {
        "Sorted": sorted_data,
        "Reverse Sorted": reverse_data,
        "Random": random_data
    }

    print("Benchmarking Sorting Algorithms\n")
    for name, func in algorithms.items():
        print(f"{name}:")
        for d_name, dataset in datasets.items():
            times = []
            for _ in range(5):
                t = time_sort(func, dataset)
                times.append(t)
            avg_time = sum(times) / len(times)
            print(f"  {d_name}: {avg_time:.4f} seconds")
        print()

if __name__ == "__main__":
    main()