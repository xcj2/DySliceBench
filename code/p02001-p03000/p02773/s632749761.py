import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
from collections import Counter
def main():
    N = I()
    s_list = []
    for i in range(N):
        s = S()
        s_list.append(s)
    c = Counter(s_list)
    a = max(c.values())
    ans_list = []
    for key in c.keys():
        if c[key] == a:
            ans_list.append(key)
    ans_list.sort()
    for ans in ans_list:
        print(ans)



if __name__ == "__main__":
    main()
