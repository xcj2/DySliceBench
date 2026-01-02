from heapq import heappush, heappop
import queue
import re
import math
import functools

def s_raw():
    return input().rstrip("\r")

def int_raw():
    return int(input())


def ss_raw():
    return input().split()


def ints_raw():
    return list(map(int, ss_raw()))


INF = 1 << 29


def make1d_arr(n, val=INF):
    return [val for i in range(n)]


def make2d_arr(h, w, val=INF):
    return [[val for i in range(w)]for i in range(h)]


def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)


def BFord(n,es):
    v_cost = [INF]*n
    v_cost[0] = 0
    for v in range(n*2):
        for e in es:
            frm = e[0]
            to = e[1]
            if v_cost[to] > v_cost[frm]+e[2]:
                v_cost[to] = v_cost[frm]+e[2]
                if v >= n:
                    v_cost[to] = -INF
        if v == n-1:
            prev = v_cost[:]
    v_cost = [-INF if prev[idx]!=v_cost[idx] else v_cost[idx] for idx in range(n)]
    return v_cost
    

def main():
    N,K,Q = ints_raw()
    As = [int_raw() for _ in range(Q)]
    Ps = [0]*N
    for a in As:
        Ps[a-1]+=1
    
    for p in Ps:
        if K-(Q-p)>0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
