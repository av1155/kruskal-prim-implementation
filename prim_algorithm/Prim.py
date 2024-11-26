"""
Prim's Algorithm Implementation for Minimum Spanning Tree (MST)

This program reads a weighted undirected graph and computes its MST using Prim's algorithm.
It uses a priority queue to efficiently select the next edge with the minimum weight.

Usage:
    python Prim.py [input_file]

Input:
    The program reads the graph from a file or standard input.
    The graph is represented as an adjacency list with weights.

    The input format is:
        n m
        u1 v1 w1
        u2 v2 w2
        ...
        um vm wm

    where:
        - n: number of vertices (vertices are labeled from 0 to n-1)
        - m: number of edges
        - ui vi wi: edge between vertex ui and vi with weight wi

Output:
    The edges in the MST and the total weight of the MST.

Example:
    Input (graph.txt):
        4 5
        0 1 10
        0 2 6
        0 3 5
        1 3 15
        2 3 4

    Command:
        python Prim.py graph.txt

    Output:
        Edges in the MST:
        0 - 3: 5.0
        3 - 2: 4.0
        0 - 1: 10.0
        Total weight of MST: 19.0
"""

import heapq
import sys


def prim(n, adj):
    """Compute the MST of a graph using Prim's algorithm.

    Args:
        n (int): Number of vertices.
        adj (list): Adjacency list where adj[u] is a list of tuples (v, w).

    Returns:
        tuple: A tuple containing:
            - mst_edges (list): List of edges in the MST.
            - total_weight (float): Total weight of the MST.
    """
    visited = [False] * n
    min_heap = []

    # Start from vertex 0
    visited[0] = True
    for v, w in adj[0]:
        heapq.heappush(min_heap, (w, 0, v))

    mst_edges = []
    total_weight = 0.0

    while min_heap and len(mst_edges) < n - 1:
        w, u, v = heapq.heappop(min_heap)
        if not visited[v]:
            visited[v] = True
            mst_edges.append((u, v, w))
            total_weight += w
            for to, weight in adj[v]:
                if not visited[to]:
                    heapq.heappush(min_heap, (weight, v, to))

    return mst_edges, total_weight


def main():
    """Main function to read input and compute MST."""
    # Read input from file or standard input
    if len(sys.argv) > 1:
        # Read from file
        with open(sys.argv[1], "r") as f:
            lines = f.readlines()
    else:
        # Read from standard input
        lines = sys.stdin.readlines()

    n, m = map(int, lines[0].split())
    adj = [[] for _ in range(n)]
    for line in lines[1:]:
        u, v, w = map(float, line.strip().split())
        u = int(u)
        v = int(v)
        adj[u].append((v, w))
        adj[v].append((u, w))  # Since the graph is undirected

    # Compute MST using Prim's algorithm
    mst_edges, total_weight = prim(n, adj)

    # Output the result
    print("Edges in the MST:")
    for u, v, w in mst_edges:
        print(f"{u} - {v}: {w}")
    print(f"Total weight of MST: {total_weight}")


if __name__ == "__main__":
    main()
