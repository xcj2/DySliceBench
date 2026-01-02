import sys
import math
import collections
import itertools
import array
import inspect

# Set max recursion limit
sys.setrecursionlimit(1000000)


def li_input():
    return [int(_) for _ in input().split()]

"""
1  insertionSort(A, n, g)
2      for i = g to n-1
3          v = A[i]
4          j = i - g
5          while j >= 0 && A[j] > v
6              A[j+g] = A[j]
7              j = j - g
8              cnt++
9          A[j+g] = v
10
11 shellSort(A, n)
12     cnt = 0
13     m = ?
14     G[] = {?, ?,..., ?}
15     for i = 0 to m-1
16         insertionSort(A, n, G[i])
"""

cnt = 0

def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v

def shellSort(A, n):
    m = 1

    G = [1]
    for i in range(1, 10000):
        if 3 * G[i - 1] + 1 > len(A):
            break
        G.append(3 * G[i - 1] + 1)
    G = G[::-1]
    m = len(G)

    print(m)
    print(" ".join(list(map(str, G))))

    for i in range(m):
        insertionSort(A, n, G[i])
    
    print(cnt)

    for a in A:
        print(a)

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    
    shellSort(A, N)



main()

