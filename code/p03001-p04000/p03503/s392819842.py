import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

def count_one(bit):
    n = 0
    while bit:
        n += (1 & bit)
        bit = bit >> 1
    return n

def main():
    N = I()
    F_bit = []
    P = []
    ans = -inf
    for i in range(N):
        f = LS()
        f_bit = int(''.join(f), base=2)
        F_bit.append(f_bit)

    for _ in range(N):
        p = LI()
        P.append(p)

    for bit in range(1, 1<<10):
        cur_ans = 0
        for i in range(N):
            i_bit = F_bit[i]
            ci = count_one(bit & i_bit)
            cur_ans += P[i][ci]
        ans = max(ans, cur_ans)
    print(ans)

    '''
    for i in range(N):
        n_open = n_open_time[i]
        i_max_prof = -1
        ix_max_prof = 0
        for j in range(n_open+1):
            if i_max_prof <= P[i][j]:
                i_max_prof = P[i][j]
                ix_max_prof = j
        cur_ans += i_max_prof
        selected_ix.add(ix_max_prof)
        if n_open > 0:
            least_ans = max(least_ans, max(P[i][1:n_open+1]))
    if len(selected_ix) == 1 and 0 in selected_ix:
        print(least_ans)
    else:
    '''

main()

