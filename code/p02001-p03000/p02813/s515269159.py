import sys
input = sys.stdin.readline
import bisect
from collections import deque


def read():
    N = int(input().strip())
    P = list(map(int, input().strip().split()))
    Q = list(map(int, input().strip().split()))
    return N, P, Q


def next_permutation(a):
    l = -1
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            l = i
    if l == -1:
        return False
    for j in range(len(a)-1, -1, -1):
        if a[l] < a[j]:
            break
    tmp = a[l]
    a[l] = a[j]
    a[j] = tmp
    j = l + 1
    k = len(a) - 1
    while j < k:
        tmp = a[k]
        a[k] = a[j]
        a[j] = tmp
        j += 1
        k -= 1
    return True


def solve(N, P, Q):
    a, b = 0, 0
    while next_permutation(P):
        a += 1
    while next_permutation(Q):
        b += 1
    return abs(b - a)
            
    
if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("{}".format(outputs))
