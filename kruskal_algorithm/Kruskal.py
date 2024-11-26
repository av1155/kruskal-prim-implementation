"""
Kruskal's Algorithm Implementation for Minimum Spanning Tree (MST)

This program reads a weighted undirected graph and computes its MST using Kruskal's algorithm.
It uses a Union-Find (Disjoint Set Union) data structure to efficiently detect cycles.

Usage:
    python Kruskal.py [input_file]

Input:
    The program reads the graph from a file or standard input.
    The graph is represented as a list of edges with their weights.

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
        python Kruskal.py graph.txt

    Output:
        Edges in the MST:
        2 - 3: 4.0
        0 - 3: 5.0
        0 - 1: 10.0
        Total weight of MST: 19.0
"""

import sys


class UnionFind:
    """
    Disjoint Set Union (Union-Find) data structure implementation.

    Attributes:
        parent (list): Parent of each element in the set.
        rank (list): Rank of each element to keep the tree flat.
    """

    def __init__(self, n):
        """Initialize Union-Find data structure with n elements.

        Args:
            n (int): Number of elements.
        """
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        """Find the representative of the set that u is a member of.

        Args:
            u (int): Element to find.

        Returns:
            int: Representative of the set.
        """
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        """Union the sets that contain u and v.

        Args:
            u (int): First element.
            v (int): Second element.

        Returns:
            bool: True if union was successful, False if u and v are already in the same set.
        """
        u_root = self.find(u)
        v_root = self.find(v)

        if u_root == v_root:
            return False  # u and v are already in the same set

        # Union by rank to keep tree shallow
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1
        return True


def kruskal(n, edges):
    """Compute the MST of a graph using Kruskal's algorithm.

    Args:
        n (int): Number of vertices.
        edges (list): List of tuples (u, v, w) representing edges.

    Returns:
        tuple: A tuple containing:
            - mst_edges (list): List of edges in the MST.
            - total_weight (float): Total weight of the MST.
    """
    # Sort edges in non-decreasing order of weight
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(n)
    mst_edges = []
    total_weight = 0.0

    for u, v, w in edges:
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            total_weight += w

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
    edges = []
    for line in lines[1:]:
        u, v, w = map(float, line.strip().split())
        edges.append((int(u), int(v), w))

    # Compute MST using Kruskal's algorithm
    mst_edges, total_weight = kruskal(n, edges)

    # Output the result
    print("Edges in the MST:")
    for u, v, w in mst_edges:
        print(f"{u} - {v}: {w}")
    print(f"Total weight of MST: {total_weight}")


if __name__ == "__main__":
    main()
