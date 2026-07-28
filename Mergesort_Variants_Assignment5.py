"""
Mergesort Variants (k-way merge) — Assignment 5
================================================
My submission for the fifth assignment of my Data Structures & Algorithms course.

Here I implemented a k-way merge sort: instead of splitting the array into 2 parts,
it splits into k parts (k >= 2), sorts each part recursively, and merges them back
together. Sub-arrays shorter than k are sorted directly with a simple sort.

--------------------------------------------------------------------------------
ANALYSIS (my own)
--------------------------------------------------------------------------------
My algorithm divides the given array into k arrays with k >= 2 and sorts each one
recursively, then merges them. It uses the sort() function (or any elementary sort)
for arrays whose length is smaller than k, because those cannot be divided by k.
All other arrays are sorted recursively by dividing them into k parts and merging
the sorted sub-arrays.

For each sort operation the function calls itself k times, each call on N/k of the
array, and then does 1 merge. The number of recursive levels is how many times N
can be divided by k before reaching 1, i.e. log_k(N). The merge function does about
k*N comparisons each time it is called, because it compares the head of each
sub-array for every position.

=> Overall complexity: O(k * N * log_k(N))

Hypothesis: the best k should be one of the smaller values, because as k grows the
recursion depth gets smaller, but each merge costs more.

--------------------------------------------------------------------------------
EXPERIMENTAL RESULTS
--------------------------------------------------------------------------------
Running the sort for different array sizes N and values of k (runtime in seconds):

    k    | N=1000  | N=5000  | N=10000
    -----+---------+---------+---------
    2    | 0.00447 | 0.02655 | 0.05825
    3    | 0.00347 | 0.01773 | 0.04462
    4    | 0.00250 | 0.01518 | 0.03233
    5    | 0.00260 | 0.01555 | 0.02842
    8    | 0.00238 | 0.01630 | 0.03113
    10   | 0.00161 | 0.01216 | 0.02373   <-- fastest for every N
    16   | 0.00397 | 0.01839 | 0.03474
    32   | 0.00245 | 0.01830 | 0.03912

Conclusion: for every array size tested, k = 10 gave the shortest runtime, and all
results were verified as correctly sorted. So the best value of k here is 10.

Author: Mohamed Farouk Ben Salem
"""

import random
import time


def merge(a, aux, lo, hi, k):
    aux[lo:hi+1] = a[lo:hi+1]
    pas = (hi+1-lo)//k
    l = [i for i in range(lo, hi, pas)][:k]
    ends = []
    for index in range(len(l)):
        if index != len(l)-1:
            ends.append(l[index]+pas-1)
        else:
            ends.append(hi)
    for e in range(lo, hi+1):
        min_index = 0
        for j in range(len(l)):
            if aux[l[j]] < aux[l[min_index]]:
                min_index = j
        a[e] = aux[l[min_index]]
        if l[min_index] < ends[min_index]:
            l[min_index] += 1
        else:
            l = l[:min_index]+l[min_index+1:]
            ends = ends[:min_index]+ends[min_index+1:]
    return a


def sorting(a, aux, lo, hi, k):
    if k < 2:
        raise ValueError("k must be at least 2")
    if lo == hi:
        return
    elif hi-lo+1 <= k:
        a[lo:hi+1] = sorted(a[lo:hi+1])
        return
    else:
        pas = (hi+1-lo)//k
        l3 = [i for i in range(lo, hi, pas)][:k]
        for i in l3:
            nlo = i
            if i != l3[-1]:
                nhi = i+pas-1
            else:
                nhi = hi
            sorting(a, aux, nlo, nhi, k)
        merge(a, aux, lo, hi, k)


# Experiment: measure runtime for different N and k, and find the best k
if __name__ == "__main__":
    for n in [1000, 5000, 10000]:
        print("N=", n)
        a1 = [random.randint(0, 100000) for i in range(n)]
        min = 100000000000000000000000
        kmin = 0
        for k in [2, 3, 4, 5, 8, 10, 16, 32]:
            a = a1.copy()
            aux = [None]*len(a)
            start = time.time()
            sorting(a, aux, 0, len(a)-1, k)
            end = time.time()
            if round(end-start, 5) < min:
                min = round(end-start, 5)
                kmin = k
            print("k=", k, "time=", round(end-start, 5), "correct=", a == sorted(a1))
        print("the minimum time is:", min, "and the best k is:", kmin)
