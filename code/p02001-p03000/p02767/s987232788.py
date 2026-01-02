import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
import bisect
def main():
    N = I()
    X = LI()
    Ans_list = []
    for i in range(1, 101):
        cnt = 0
        for x in X:
            cnt += (x - i) ** 2
        Ans_list.append(cnt)
    print(min(Ans_list))

if __name__ == "__main__":
    main()
