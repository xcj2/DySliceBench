#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]
        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a)-i)
    c += a[i:]
    c += b[j:]
    return c, inversions

def mergeAndCountSplitInv(c, d):
    # c: left half, d: right half, both sorted
    nc = len(c)
    nd = len(d)
    b = [0] * (nc + nd)
    i, j = 0, 0
    splitInv = 0
    for k in range((nc + nd)):
        if i == nc: # c is used up
            b[k] = d[j]
            j += 1
            continue
        if j == nd: # d is used up
            b[k] = c[i]
            i += 1
            continue

        if c[i] <= d[j]: 
            b[k] = c[i]
            i += 1
        elif c[i] > d[j]:
            b[k] = d[j]
            splitInv += nc - i
            j += 1
    return b, splitInv

def sortCountInv(a):
    # a: list of int
    n = len(a)
    if n <= 1: # base case
        return a, 0
    c, leftInv = sortCountInv(a[ : n//2])
    d, rightInv = sortCountInv(a[n//2: ])
    b, splitInv = mergeAndCountSplitInv(c, d)
    # print(leftInv, rightInv, splitInv)
    return b, leftInv + rightInv + splitInv

def solve(N: int, K: int, A: "List[int]"):
    A_sort, inv = mergeSortInversions(A)
    t = [0] * N
    for i in range(1, N):
        if A_sort[i] > A_sort[i-1]:
            t[i] = i
        else:
            t[i] = t[i-1]
    count = inv * K + sum(t) * (K * (K-1))//2
    count = count % MOD
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
