from collections import deque
from heapq import heappush,heappop
import re

def int_raw():
    return int(input())

def ss_raw():
    return input().split()

def ints_raw():
    return list(map(int, ss_raw()))

INF = 1<<29



def main():
    N, M = ints_raw()
    CBs =[]
    CBs.append([0,N])
    As = ints_raw()
    As.sort()
    for _ in range(M):
        B,C = ints_raw()
        CBs.append([C,B])
    CBs.sort(reverse=True)
    ans = 0
    cb_idx = 0
    cur_cbs = CBs[cb_idx]
    for a in As:
        if a < cur_cbs[0]:
            cur_cbs[1]-=1
            ans+=cur_cbs[0]
            if cur_cbs[1] <=0:
                cb_idx+=1
                cur_cbs = CBs[cb_idx]
        else:
            ans+=a
    return ans

print(main())
