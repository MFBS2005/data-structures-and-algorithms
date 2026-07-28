# Data Structures & Algorithms

Assignments from my Data Structures & Algorithms (DSA) course during my studies.
Each notebook contains my solutions to the exercises — both the written analysis
and the code implementations.

I'm sharing these because they show the theoretical side of my work: understanding
how data structures behave, analyzing time complexity, and reasoning about why one
approach is faster than another — not just writing code that runs.

The code and written answers are kept as I originally submitted them. Where I added
context or notes, I say so explicitly.

## Assignments

### Assignment 1 — Union-Find
`UnionFind_Assignment1.ipynb`

The Union-Find (disjoint set) structure. Covers the correctness of quick-find and
weighted quick-union, with written analysis of why certain implementations are or
aren't correct.

### Assignment 2 — Stacks, Queues & Deques
`Stacks_Queues_Deques_Assignment2.ipynb`

FIFO/LIFO principles, the behaviour of stacks and queues (including edge cases such
as popping an empty stack), a decimal-to-binary conversion using a stack, reversing
a queue using a stack, and an iterative Fibonacci exercise.

### Assignment 4 — Elementary Sorting
`Elementary_Sorting_Assignment4.ipynb`

Selection sort, insertion sort and shell sort, a comparator (`__lt__`) for sorting
custom objects, and a binary insertion sort variant. This notebook also contains a
**detailed course summary I wrote for myself** while studying the topic — it covers
the algorithms, their complexities, inversions, Shellsort increment sequences, and
the Knuth–Fisher–Yates shuffle.

### Assignment 5 — Mergesort Variants (k-way merge)
`Mergesort_Variants_Assignment5.ipynb`

A k-way merge sort: splitting the array into k parts instead of 2, sorting each
recursively, and merging them. Includes my own complexity analysis
(O(kN·log_k N)), a hypothesis about the best value of k, and experiments to test it.

## Technologies

Python 3 (Jupyter / Google Colab notebooks).

## Note

These are coursework assignments, so parts of the setup code (test harnesses, file
loading) were provided as part of the course. My own work is in the solutions and
the written analysis. I've kept everything authentic rather than rewriting it.
