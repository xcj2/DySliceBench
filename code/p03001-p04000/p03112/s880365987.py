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
     
def main():
    A, B, Q = LI()
    s = []
    t = []
    x = []
    for _ in range(A):
        s.append(I())
    for _ in range(B):
        t.append(I())
    for _ in range(Q):
        x.append(I())

    # ダミー境界を加える
    s = [-inf] + s + [inf]
    t = [-inf] + t + [inf]

    for pos in x:
        l_s = bisect.bisect_left(s, pos)
        l_t = bisect.bisect_left(t, pos)

        left_shrine = s[l_s-1]
        right_shrine = s[l_s]
        left_temple = t[l_t-1]
        right_temple = t[l_t]

        d1 = pos - min(left_shrine, left_temple)
        d2 = max(right_shrine, right_temple) - pos
        d3 = 2 * (pos - left_shrine) + (right_temple - pos)
        d4 = 2 * (right_temple - pos) + (pos - left_shrine)
        d5 = 2 * (pos - left_temple) + (right_shrine - pos)
        d6 = 2 * (right_shrine - pos) + (pos - left_temple)

        ans = min([
            d1, d2, d3, d4, d5, d6
        ])
        print(ans)

    '''
    ダミー境界を加えない場合
    for pos in x:
        l_s = bisect.bisect_left(s, pos)
        l_t = bisect.bisect_left(t, pos)

        if l_s == 0:
            left_shrine = None
        else:
            left_shrine = s[l_s-1]
        if l_s == A:
            right_shrine = None
        else:
            right_shrine = s[l_s]

        if l_t == 0:
            left_temple = None
        else:
            left_temple = t[l_t-1]
        if l_t == B:
            right_temple = None
        else:
            right_temple = t[l_t]

        d1, d2, d3, d4, d5, d6 = inf, inf, inf, inf, inf, inf
        if left_shrine and left_temple:
            d1 = pos - min(left_shrine, left_temple)
        if right_shrine and right_temple:
            d2 = max(right_shrine, right_temple) - pos
        if left_shrine and right_temple:
            d3 = 2 * (pos - left_shrine) + (right_temple - pos)
            d4 = 2 * (right_temple - pos) + (pos - left_shrine)
        if left_temple and right_shrine:
            d5 = 2 * (pos - left_temple) + (right_shrine - pos)
            d6 = 2 * (right_shrine - pos) + (pos - left_temple)

        ans = min([
            d1, d2, d3, d4, d5, d6
        ])
        print(ans)
        '''
main()

