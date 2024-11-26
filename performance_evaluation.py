"""
Performance Evaluation of Kruskal's and Prim's Algorithms

This script generates random graphs of varying sizes and densities to empirically
evaluate and compare the performance (execution time) of Kruskal's and Prim's algorithms.

Usage:
    python performance_evaluation.py

Requirements:
    - Python 3.x
    - matplotlib (for plotting results)
    - NetworkX (for generating random graphs)
    - pandas (for exporting data to CSV)
"""

import random
import time

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

from kruskal_algorithm.Kruskal import kruskal
from prim_algorithm.Prim import prim


def generate_random_graph(n, m):
    """Generate a random undirected weighted graph.

    Args:
        n (int): Number of vertices.
        m (int): Number of edges.

    Returns:
        list: List of edges in the format (u, v, w).
        list: Adjacency list for Prim's algorithm.
    """
    G = nx.gnm_random_graph(n, m)
    edges = []
    adj = [[] for _ in range(n)]
    for u, v in G.edges():
        w = random.uniform(1, 100)
        edges.append((u, v, w))
        adj[u].append((v, w))
        adj[v].append((u, w))
    return edges, adj


def evaluate_performance():
    """Evaluate and compare the performance of Kruskal's and Prim's algorithms."""
    num_vertices = [50, 100, 200, 300, 400, 500]
    densities = [0.1, 0.3, 0.5, 0.7, 0.9]
    data = []

    for n in num_vertices:
        for density in densities:
            m = int(
                density * n * (n - 1) / 2
            )  # Maximum number of edges in an undirected graph
            edges, adj = generate_random_graph(n, m)

            # Time Kruskal's algorithm
            start_time = time.time()
            kruskal(n, edges.copy())
            kruskal_time = time.time() - start_time

            # Time Prim's algorithm
            start_time = time.time()
            prim(n, adj)
            prim_time = time.time() - start_time

            print(
                f"n={n}, density={density:.1f}, Kruskal Time={kruskal_time:.4f}s, Prim Time={prim_time:.4f}s"
            )

            # Append results to the data list
            data.append(
                {
                    "Vertices": n,
                    "Density": density,
                    "Kruskal_Time": kruskal_time,
                    "Prim_Time": prim_time,
                }
            )

    # Save data to a CSV file
    df = pd.DataFrame(data)
    df.to_csv("results/performance_results.csv", index=False)
    print("Results saved to results/performance_results.csv")

    # Plotting the results
    for n in num_vertices:
        subset = df[df["Vertices"] == n]
        plt.figure(figsize=(10, 6))
        plt.plot(
            subset["Density"],
            subset["Kruskal_Time"],
            label="Kruskal's Algorithm",
            marker="o",
        )
        plt.plot(
            subset["Density"], subset["Prim_Time"], label="Prim's Algorithm", marker="s"
        )
        plt.title(f"Performance Comparison for n={n}")
        plt.xlabel("Density")
        plt.ylabel("Execution Time (seconds)")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"results/performance_n_{n}.png")
        plt.close()


if __name__ == "__main__":
    evaluate_performance()
