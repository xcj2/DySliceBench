import sys, math, collections, heapq, itertools
from bisect import bisect_left
F = sys.stdin
def single_input(): return F.readline().strip("\n")
def line_input(): return F.readline().strip("\n").split()
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b > 0: a, b = b, a % b
    return b
  
def solve():
    Q = int(single_input())
    n, a, b = map(int, line_input())
    left, right = [-a], [a]
    heapq.heapify(left)
    heapq.heapify(right)
    minans =  b
    for i in range(1, Q):
        queri = [int(i) for i in line_input()]
        if queri[0] == 1:
            a, b = queri[1:]
            minans += b
            left_upper = -1 * heapq.heappop(left)
            right_lower = heapq.heappop(right)
            if left_upper <= a <= right_lower:
                heapq.heappush(left, -a)
                heapq.heappush(left, -1 * left_upper)
                heapq.heappush(right, a)
                heapq.heappush(right, right_lower)
            elif a < left_upper:
                minans += left_upper - a
                heapq.heappush(left, -a)
                heapq.heappush(left, -a)
                heapq.heappush(right, left_upper)
                heapq.heappush(right, right_lower)
            else:
                minans += a - right_lower
                heapq.heappush(left, -1 * left_upper)
                heapq.heappush(left, -1 * right_lower)
                heapq.heappush(right, a)
                heapq.heappush(right, a)
        else:
            left_lower = -1 * heapq.heappop(left)
            print(left_lower, minans)
            heapq.heappush(left, -1 * left_lower)
    return 0
  
if __name__ == "__main__":
    solve()