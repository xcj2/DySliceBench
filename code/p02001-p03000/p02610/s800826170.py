import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


def init(bit, values):
    for i,v in enumerate(values):
        add(bit,i+1,v)
#a1 ~ aiまでの和 O(logn)
def query(bit,i):
    res = 0
    while i > 0:
        res += bit[i]
        i -= i&(-i)
    return res

#ai += x(logN)
def add(bit,i,x):
    if i==0:
        raise RuntimeError
    while i <= len(bit)-1:
        bit[i] += x
        i += i&(-i)
    return


t = int(input())
ANS = [None]*t
from collections import defaultdict
from heapq import heappop as hpp, heappush as hp
for iii in range(t):
    n = int(input())
    d1 = defaultdict(list)
    d0 = defaultdict(list)
    lr = [None]*n
    for i in range(n):
        k,l,r = list(map(int, input().split()))
        lr[i] = (l,r)
        if l-r>=0:
            d1[k].append((l-r, i))
        else:
            d0[k].append((r-l, i))
            
    sl = set()
    sr = set()
    h = []
    for i in range(1,n+1):
        if i not in d1:
            continue
        for item in d1[i]:
            hp(h, item)
        while i<len(h):
            *_,ii = hpp(h)
            sr.add(ii)
    for *_,i in h:
        sl.add(i)
    h = []
    for i in range(n, 0, -1):
        if i not in d0:
            continue
        for item in d0[i]:
            hp(h,item)
        while (n-i)<len(h):
            *_,ii = hpp(h)
            sl.add(ii)
    for *_,i in h:
        sr.add(i)
    ans = 0
#     print(lr0, lr1, sl, sr)
    for i in sl:
        ans += lr[i][0]
    for i in sr:
        ans += lr[i][1]
    ANS[iii] = ans
write("\n".join(map(str, ANS)))