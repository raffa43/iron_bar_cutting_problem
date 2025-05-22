import random
import sys
import time

import matplotlib.pyplot as plt
import numpy as np

from bottom_up import corte_barra_bottom_up
from dynamic_top_down import dynamic_top_down_solution
from greedy import greedy_solution

sys.setrecursionlimit(10**9)


def generate_random_price_data(size):
    return {i: random.randint(1, 9999) for i in range(1, size + 1)}


def benchmark_algorithms():
    """Benchmark all algorithms with increasing price data sizes"""
    sizes = [
        100,
        1000,
        2000,
        5000,
        8000,
        10000,
        25000,
        50000,
    ]
    results = {"greedy": [], "top_down": [], "bottom_up": []}

    for size in sizes:
        print(f"\nBenchmarking with size {size}:")

        price_data = generate_random_price_data(size)

        start = time.time()
        try:
            greedy_solution(size, price_data)
            end = time.time()
            elapsed = end - start
            results["greedy"].append(elapsed)
            print(f"  Greedy solution: {elapsed:.6f} seconds")
        except Exception as e:
            print(f"  Greedy solution failed: {str(e)}")
            results["greedy"].append(None)

        time.sleep(0.5)
        start = time.time()
        try:
            dynamic_top_down_solution(size, price_data)
            end = time.time()
            elapsed = end - start
            results["top_down"].append(elapsed)
            print(f"  Top-down solution: {elapsed:.6f} seconds")
        except Exception as e:
            print(f"  Top-down solution failed: {str(e)}")
            results["top_down"].append(None)

        time.sleep(0.5)
        start = time.time()
        try:
            corte_barra_bottom_up(size, price_data)
            end = time.time()
            elapsed = end - start
            results["bottom_up"].append(elapsed)
            print(f"  Bottom-up solution: {elapsed:.6f} seconds")
        except Exception as e:
            print(f"  Bottom-up solution failed: {str(e)}")
            results["bottom_up"].append(None)

    plt.figure(figsize=(14, 8))

    for method, times in results.items():
        valid_data = [
            (size, time) for size, time in zip(sizes, times) if time is not None
        ]
        if valid_data:
            plot_sizes, plot_times = zip(*valid_data)
            plt.plot(
                plot_sizes,
                plot_times,
                marker="o",
                linewidth=2,
                label=method.replace("_", "-"),
            )

    plt.xscale("log")
    plt.xticks(sizes, [str(size) for size in sizes], rotation=45)

    plt.yscale("linear")

    plt.gca().yaxis.set_major_formatter(
        plt.matplotlib.ticker.StrMethodFormatter("{x:.4f}")
    )

    plt.xlabel("Size of Price Data")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Performance Comparison of Iron Bar Cutting Algorithms")
    plt.legend()
    plt.grid(True, which="both", ls="--", alpha=0.7)

    plt.tight_layout()
    plt.savefig("performance_comparison.png")
    plt.show()

    return results


if __name__ == "__main__":
    benchmark_results = benchmark_algorithms()
    print("\nResults summary:")
    for method, times in benchmark_results.items():
        valid_times = [t for t in times if t is not None]
        if valid_times:
            print(f"  {method}: {valid_times}\n")
