import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
def main():
    N, M = MI()
    D = defaultdict(int)
    for i in range(1, N + 1):
        D[i] = None
    for i in range(M):
        s, c = MI()
        if D[s] == None:
            D[s] = c
        elif D[s] != c:
            print(-1)
            exit()
    ans_list = []
    for i in range(1,N + 1):
        a = D[i]
        if a == None and i == 1 and N != 1:
            a = 1
        if a == None and i == 1 and N == 1:
            a = 0
        if a == None and i != 1:
            a = 0
        ans_list.append(a)
    if N != 1 and ans_list[0] == 0:
        print(-1)
        exit()
    print(''.join(map(str, ans_list)))


if __name__ == "__main__":
    main()