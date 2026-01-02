import sys
#import copy
#import numpy as np
#import itertools
#import collections
#from collections import deque
#from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
#from scipy.sparse import csr_matrix
import functools

sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
#read = sys.stdin.buffer.read

def gcd(nums):
    return functools.reduce(euclid, nums)

def euclid(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

def main():
    # input
    K = int(readline())

    ans = 0
    for i in range(1, K+1):
        for j in range(1, K+1):
            for k in range(1, K+1):
                ans += gcd([i,j,k])
    
    print(ans)


if __name__ == "__main__":
    main()
