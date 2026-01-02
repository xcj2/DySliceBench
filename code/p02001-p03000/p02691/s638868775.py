import sys
sys.setrecursionlimit(10**6) #再帰関数の上限
import math
from copy import copy, deepcopy
from operator import itemgetter

from bisect import bisect_left, bisect, bisect_right#2分探索
#bisect_left(l,x), bisect(l,x)#aはソート済みである必要あり。aの中からx未満の要素数を返す。rightだと以下
from collections import deque 
#deque(l), pop(), append(x), popleft(), appendleft(x)
##listでqueの代用をするとO(N)の計算量がかかってしまうので注意
#dequeを使うときはpython3を使う、pypyはダメ
from collections import Counter#文字列を個数カウント辞書に、
#S=Counter(l),S.most_common(x),S.keys(),S.values(),S.items()
from itertools import accumulate#累積和
#list(accumulate(l))
from heapq import heapify,heappop,heappush
#heapify(q),heappush(q,a),heappop(q) #q=heapify(q)としないこと、返り値はNone

def input(): return sys.stdin.readline()[:-1]
def printl(li): print(*li, sep="\n")
def argsort(s, return_sorted=False): 
    inds=sorted(range(len(s)), key=lambda k: s[k])
    if return_sorted: return inds, [s[i] for i in inds]
    return inds

#mod = 10**9+7
#w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

N = int(input())
#N, K = map(int, input().split())
#L = [int(input()) for i in range(N)]
A = list(map(int, input().split()))
#S = [list(map(int, input().split())) for i in range(N)]

Am=copy(A)
for i, a in enumerate(A):
    Am[i]=i+1-a
Am.sort()

ans=0
for i, a in enumerate(A):
    x=a+i+1
    count=bisect_right(Am,x)-bisect_left(Am,x)

    ans+=count
print(ans)
