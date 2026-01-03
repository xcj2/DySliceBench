import sys, math, collections, heapq, itertools
from bisect import bisect
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0:
        a, b = b, a % b
    return b
  
def solve():
    X, Y = map(int, line_input())
    p = [0] * X
    q = [0] * Y
    for x in range(X): p[x] = int(single_input())
    for y in range(Y): q[y] = int(single_input())
    total_cost = sum(p) + sum(q)
    p.sort()
    total_sum_p = [0] * (X + 1)
    for x in range(X):
        total_sum_p[x+1] = p[x] + total_sum_p[x]
    for y in range(Y):
        x_smaller_than_y = bisect(p, q[y])
        total_cost += q[y] * (X - x_smaller_than_y) + total_sum_p[x_smaller_than_y]
    return total_cost
  
if __name__ == "__main__":
    print(solve())