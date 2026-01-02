import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
from collections import Counter
import bisect
def main():
    H, W, K = MI()
    C = []
    for i in range(H):
        c = S()
        C.append(c)
    A = []
    for i in range(2 ** (H + W)):
        A_bit = []
        for j in range(H + W):
            # 二進数表記でj回右にシフトして0桁目（一番下の桁）が1であればTrue
            if ((i >> j) & 1):
                A_bit.append(j)
        A.append(A_bit)
    Ans_list = []
    for a in A:
        cnt = 0
        for i in range(H):
            if i in a:
                continue
            else:
                for j in range(H, W + H):
                    if j not in a and C[i][j - H] == '#':
                        cnt += 1
        Ans_list.append(cnt)
    ans = Counter(Ans_list)[K]
    print(ans)


if __name__ == "__main__":
    main()

