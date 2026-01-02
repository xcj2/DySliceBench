import sys
# input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import math
import heapq
import fractions
from collections import defaultdict, Counter, deque
MOD = 10**9 + 7
INF = 10**15

def getyaku(n):
    res = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            res.append(i)
            res.append(n // i)

    return(sorted(list(set(res))))

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def main():
    n,m = getlist()
    wa = [0 for i in range(n)]
    ac = [0 for i in range(n)]
    ansa = 0
    ansp = 0
    for i in range(m):
        p, s = input().split()
        p = int(p) -1
        if s == "AC":
            if not ac[p]:
                ansa += 1
                ansp += wa[p]
                ac[p] = 1
        else:
            wa[p] += 1

    print(ansa, ansp)

    return

if __name__ == '__main__':
    main()

"""
9999
3

2916
"""