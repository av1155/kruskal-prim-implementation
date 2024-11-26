# User Manual for Minimum Spanning Tree Algorithms

-   [User Manual for Minimum Spanning Tree Algorithms](#user-manual-for-minimum-spanning-tree-algorithms)
    -   [Kruskal's Algorithm](#kruskals-algorithm)
        -   [Kruskal's Algorithm Usage](#kruskals-algorithm-usage)
        -   [Kruskal's Algorithm Input Format](#kruskals-algorithm-input-format)
            -   [Kruskal's Algorithm Example:](#kruskals-algorithm-example)
            -   [Kruskal's Algorithm Sample Run:](#kruskals-algorithm-sample-run)
    -   [Prim's Algorithm](#prims-algorithm)
        -   [Prim's Algorithm Usage](#prims-algorithm-usage)
        -   [Prim's Algorithm Input Format](#prims-algorithm-input-format)
            -   [Prim's Algorithm Example](#prims-algorithm-example)
            -   [Prim's Algorithm Sample Run:](#prims-algorithm-sample-run)

This user manual provides instructions on how to use the implementations of Kruskal's and Prim's algorithms for computing the Minimum Spanning Tree (MST) of an undirected, weighted graph.

---

## Kruskal's Algorithm

This implementation computes the MST of a given undirected, weighted graph using Kruskal's algorithm.

### Kruskal's Algorithm Usage

To run the program, use the following command:

```bash
python Kruskal.py [input_file]
```

-   If `input_file` is provided, the program reads the graph from the specified file.
-   If `input_file` is not provided, the program reads the graph from standard input.

### Kruskal's Algorithm Input Format

The input graph should be provided in the following format:

```txt
n m
u1 v1 w1
u2 v2 w2
...
um vm wm
```

-   `n`: Number of vertices (vertices are labeled from `0` to `n-1`)
-   `m`: Number of edges
-   `ui vi wi`: Edge between vertex `ui` and `vi` with weight `wi`

**Output:**

-   A list of edges included in the MST.
-   The total weight of the MST.

#### Kruskal's Algorithm Example:

Input file `graph.txt`:

```txt
4 5
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4
```

#### Kruskal's Algorithm Sample Run:

```bash
python Kruskal.py graph.txt
```

**Output:**

```txt
Edges in the MST:
2 - 3: 4.0
0 - 3: 5.0
0 - 1: 10.0
Total weight of MST: 19.0
```

---

## Prim's Algorithm

This implementation computes the MST of a given undirected, weighted graph using Prim's algorithm.

### Prim's Algorithm Usage

To run the program, use the following command:

```bash
python Prim.py [input_file]
```

-   If `input_file` is provided, the program reads the graph from the specified file.
-   If `input_file` is not provided, the program reads the graph from standard input.

### Prim's Algorithm Input Format

The input graph should be provided in the following format:

```txt
n m
u1 v1 w1
u2 v2 w2
...
um vm wm
```

-   `n`: Number of vertices (vertices are labeled from `0` to `n-1`)
-   `m`: Number of edges
-   `ui vi wi`: Edge between vertex `ui` and `vi` with weight `wi`

**Output:**

-   A list of edges included in the MST.
-   The total weight of the MST.

#### Prim's Algorithm Example

Input file `graph.txt`:

```txt
4 5
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4
```

#### Prim's Algorithm Sample Run:

```bash
python Prim.py graph.txt
```

**Output:**

```txt
Edges in the MST:
0 - 3: 5.0
3 - 2: 4.0
0 - 1: 10.0
Total weight of MST: 19.0
```

**Note:** The order of edges may differ from Kruskal's algorithm, but the total weight of the MST should be the same.

---

Feel free to run the programs with your own input files or modify the existing ones to test different graphs. The code is thoroughly documented to help you understand each step of the algorithms.
