import sys
import math
import copy
from typing import Tuple, List
input = sys.stdin.readline

def swap (A: List, i: int, j: int) -> None:
    temp = A [i]
    A [i] = A [j]
    A [j] = temp


def insertionSort(A, n, g):
    cnt = 0
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = v
    return cnt

def shellSort(A, n):
    cnt = 0
    g = []
    h = 1
    while h <= len(A):
        g.append(h)
        h = 3 * h + 1
    g.reverse()
    m = len(g)
    print(m)
    print(" ".join(map(str, g)))
    for i in range(m):
        cnt += insertionSort(A, n, g[i])
    print(cnt)


if __name__ == "__main__":
    n = int(input())
    A = []
    for i in range(n):
        A.append(int(input()))
    shellSort(A, len(A))
    for item in A:
        print(item)

