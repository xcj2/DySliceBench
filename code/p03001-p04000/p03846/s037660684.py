from collections import Counter,defaultdict
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
a = inpl()
cnt = Counter(a)
if n%2 == 0:
    for key in cnt.keys():
        if key%2 and key < n and cnt[key] == 2:
            continue
        else:
            print(0)
            quit()
    print((2**(n//2)) % mod)
else:
    for key in cnt.keys():
        if key % 2 == 0 and key < n and cnt[key] == 2:
            continue
        elif key == 0 and cnt[key] == 1:
            continue
        else:
            print(0)
            quit()
    print((2**(n//2)) % mod)