from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

def main():
    n = inp()
    s = input()
    x = 0
    res = 0
    for i,j in enumerate(s):
        if j == 'I':
            x += 1
        else:
            x -= 1
        res = max(res, x)
    print(res)
if __name__ == '__main__':
    main()