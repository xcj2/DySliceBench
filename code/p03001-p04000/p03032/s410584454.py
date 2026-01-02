import sys
input=sys.stdin.readline
from collections import deque
from heapq import heappush,heappop
import re

def int_raw():
    return int(input())
 
def ss_raw():
    return input().split()
 
def ints_raw():
    return tuple(map(int, ss_raw()))


def main():
    N ,K = ints_raw()
    Vs = ints_raw()
    N = len(Vs)
    leftSum = [0]
    leftNegas = [[]]
    for v in Vs:
        leftSum.append(leftSum[-1]+v)
        neoNega = leftNegas[-1]
        if v<0:
            neoNega = neoNega+[v]
            neoNega.sort()
        leftNegas.append(neoNega )


    rightSum = [0]
    rightNegas = [[]]
    for v in Vs[::-1]:
        rightSum.append(rightSum[-1]+v)
        neoNega = rightNegas[-1]
        if v<0:
            neoNega = rightNegas[-1]+[v]
            neoNega.sort()
        rightNegas.append(neoNega )

    ans = 0
    for left_k in range(K+1):
        left_total = 0
        left_n = 0
        for n in range(min(N+1,left_k+1)):
            tmp = leftSum[n] - (sum(leftNegas[n]) if len(leftNegas[n])<=left_k-n else sum(leftNegas[n][:left_k-n]))
            if left_total < tmp:
                left_total = tmp
                left_n = n
        right_total = 0
        right_n = 0
        right_k = K -left_k
        for n in range(min(K-left_k+1,N-left_n+1)):
            tmp = rightSum[n] - (sum(rightNegas[n]) if len(rightNegas[n])<=right_k-n else sum(rightNegas[n][:right_k-n]))
            if right_total < tmp:
                right_total = tmp
                right_n = n
        ans = max(ans,left_total+right_total)
    return ans

print(main())
