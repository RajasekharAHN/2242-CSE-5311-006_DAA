import time
import random
import matplotlib.pyplot as plt
import platform

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_indx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_indx]:
                min_indx = j
        arr[i], arr[min_indx] = arr[min_indx], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def benchmark_sort(sort_func, input_sizes):
    runtimes = []
    for size in input_sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]
        start_time = time.time()
        sort_func(arr)
        end_time = time.time()
        runtime = end_time - start_time
        runtimes.append(runtime)
    return runtimes

def plot_results(input_sizes, runtimes):
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, runtimes[0], marker='o', color='red', label='Insertion Sort')
    plt.plot(input_sizes, runtimes[1], marker='o', color='green', label='Selection Sort')
    plt.plot(input_sizes, runtimes[2], marker='o', color='blue', label='Bubble Sort')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime of Sorting Algorithms vs Input Size')
    plt.legend()
    plt.grid(True)
    plt.show()
    for i, size in enumerate(input_sizes):
        print("---------------------------")
        print("Input size:", size)
        print("Insertion Sort:", runtimes[0][i])
        print("Selection Sort:", runtimes[1][i])
        print("Bubble Sort:", runtimes[2][i])

def get_system_info():
    system_info = {}
    system_info['System Name'] = platform.node()
    system_info['Processor'] = platform.processor()
    system_info['RAM'] = "16 GB"
    return system_info

if __name__ == "__main__":
    input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]  # Add more sizes for larger arrays

    # Benchmark each sorting algorithm
    insertion_runtimes = benchmark_sort(insertion_sort, input_sizes)
    selection_runtimes = benchmark_sort(selection_sort, input_sizes)
    bubble_runtimes = benchmark_sort(bubble_sort, input_sizes)

    # Plot results
    plot_results(input_sizes, [insertion_runtimes, selection_runtimes, bubble_runtimes])

    # Get system information
    system_info = get_system_info()
    for key, value in system_info.items():
        print(key + ": " + value)
