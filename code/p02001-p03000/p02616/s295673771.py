# Template 1.0
import sys, re
from collections import deque, defaultdict, Counter, OrderedDict
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from heapq import heappush, heappop, heapify, nlargest, nsmallest
def STR(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def sortListWithIndex(listOfTuples, idx):   return (sorted(listOfTuples, key=lambda x: x[idx]))
def sortDictWithVal(passedDic):
    temp = sorted(passedDic.items(), key=lambda kv: (kv[1], kv[0]))
    toret = {}
    for tup in temp:
        toret[tup[0]] = tup[1]
    return toret
def sortDictWithKey(passedDic):
    return dict(OrderedDict(sorted(passedDic.items())))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

n, k = MAP()

a = LIST()

pos = []
neg = []
zero = []

for el in a:
    if(el<0):
        neg.append(el)
    elif(el>0):
        pos.append(el)
    else:
        zero.append(el)

pos = sorted(pos)[::-1]
neg = sorted(neg)[::-1]

ans = 1

if(k==n or k>len(pos)+len(neg)):
    for el in a:
        ans = (ans%mod*el%mod)%mod
elif(len(pos)+len(neg)==k):
    if(len(neg)%2!=0):
        ans = 0
    else:
        for el in pos:
            ans = (ans%mod*el%mod)%mod
        for el in neg:
            ans = (ans%mod*el%mod)%mod

else:

    if(len(pos)==0):
        if(k%2==0):
            temp = 0
            for i in range(len(neg)-1, -1, -1):
                if(temp==k):
                    break
                ans = (ans%mod*neg[i]%mod)%mod
                temp+=1
            if(temp<k):
                ans = 0
        else:
            temp = 0
            if(0 in a):
                ans = 0
            else:
                for i in range(len(neg) - 1):
                    if (temp == k):
                        break
                    ans = (ans%mod * neg[i]%mod) % mod
                    temp += 1
                if (temp < k):
                    ans = 0
    else:

        left = k

        i,j = 0, len(neg)-1

        while(left>1):
            temp, temp1 = 0, 0
            if(i<len(pos)-1):
                temp = pos[i]*pos[i+1]
                # i+=2
            if(j>=1):
                temp1 = neg[j]*neg[j-1]
                # j-=2
            if(temp==0 and temp1==0):
                break
            if(temp1>temp):
                ans = (ans*(temp1%mod))%mod
                j-=2
            else:
                ans = (ans*(temp%mod))%mod
                i+=2
            left -= 2
        # print(ans,i,j)
        if(left>1):
            ans = 0
        elif(left==1):
            if(i<len(pos)):
                ans = ((ans%mod)*pos[i])%mod
            else:
                ans1 = 1
                for b in range(i-1):
                    ans1 = (ans1%mod*(pos[b]))%mod
                for c in range(len(neg)-1, j-2,-1):
                    ans1 = (ans1%mod*neg[c])%mod
                ans = max(ans, ans1)
        if(k%2!=0):
            ans1 = 1
            if(i-2>=0 and j-2>=-1 and i-2<=len(pos)-1 and j-2<=len(neg)-1):
                for b in range(i-1):
                    ans1 = (ans1%mod*(pos[b]))%mod
                for c in range(len(neg)-1, j-2,-1):
                    ans1 = (ans1%mod*neg[c])%mod
            # print(ans, ans1)
            ans = max(ans, ans1)
print(ans)
