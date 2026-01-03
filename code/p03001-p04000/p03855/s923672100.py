import sys
sys.setrecursionlimit(10**7) #再帰関数の上限,10**5以上の場合python
import math
from copy import copy, deepcopy
from copy import deepcopy as dcp
from operator import itemgetter
from bisect import bisect_left, bisect, bisect_right#2分探索
#bisect_left(l,x), bisect(l,x)#aはソート済みである必要あり。aの中からx未満の要素数を返す。rightだと以下
from collections import deque, defaultdict
#deque(l), pop(), append(x), popleft(), appendleft(x)
#q.rotate(n)で → にn回ローテート
from collections import Counter#文字列を個数カウント辞書に、
#S=Counter(l),S.most_common(x),S.keys(),S.values(),S.items()
from itertools import accumulate,combinations,permutations#累積和
#list(accumulate(l))
from heapq import heapify,heappop,heappush
#heapify(q),heappush(q,a),heappop(q) #q=heapify(q)としないこと、返り値はNone
#import fractions#古いatcoderコンテストの場合GCDなどはここからimportする
from functools import reduce,lru_cache#pypyでもうごく
#@lru_cache(maxsize = None)#maxsizeは保存するデータ数の最大値、2**nが最も高効率
from decimal import Decimal

def input(): 
    x=sys.stdin.readline()
    return x[:-1] if x[-1]=="\n" else x
def printe(*x):print("## ",*x,file=sys.stderr)
def printl(li): _=print(*li, sep="\n") if li else None
def argsort(s, return_sorted=False): 
    inds=sorted(range(len(s)), key=lambda k: s[k])
    if return_sorted: return inds, [s[i] for i in inds]
    return inds
def alp2num(c,cap=False): return ord(c)-97 if not cap else ord(c)-65
def num2alp(i,cap=False): return chr(i+97) if not cap else chr(i+65)
def matmat(A,B):
    K,N,M=len(B),len(A),len(B[0])
    return [[sum([(A[i][k]*B[k][j]) for k in range(K)]) for j in range(M)] for i in range(N)]
def matvec(M,v):
    N,size=len(v),len(M)
    return [sum([M[i][j]*v[j] for j in range(N)]) for i in range(size)]
def T(M):
    n,m=len(M),len(M[0])
    return [[M[j][i] for j in range(n)] for i in range(m)]
class unionfind:#早いunionfind,class[i]のように要素指定すると親を得ることができる
    def __init__(self, elements=None):#elementsで初期化
        if elements is None:
            elements = ()
        self.parents = {}
        self.weights = {}
        for x in elements:
            self.weights[x] = 1
            self.parents[x] = x

    def __getitem__(self, i):
        # check for previously unknown i
        if i not in self.parents:
            self.parents[i] = i
            self.weights[i] = 1
            return i
        path = [i]
        root = self.parents[i]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]
        for ancestor in path:#縮約
            self.parents[ancestor] = root
        return root

    def __iter__(self):#for parent in Class:
        return iter(self.parents)

    def union(self, *objects):#オブジェクトをすべて結合
        roots = [self[x] for x in objects]
        heaviest = max(roots, key=lambda r: self.weights[r])
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest

    def __len__(self):
        return len(self.parents)

def main():
    mod = 1000000007
    #w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    #N = int(input())
    N, K, L = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
     #改行行列
    train=unionfind(range(N))
    rail=unionfind(range(N))

    for i in range(K):#木の場合M=N-1
        a,b = map(int,input().split())
        train.union(a-1,b-1)

    S = tuple(tuple(map(int, input().split())) for i in range(L))
    for a,b in S:#木の場合M=N-1
        a-=1
        b-=1
        rail.union(a,b)

    
    c=Counter()

    ans=[0]*N

    for i in range(N):
        c[rail[i]*N+train[i]]+=1
    for i in range(N):
        ans[i]=c[rail[i]*N+train[i]]
    print(*ans)
        
    





if __name__ == "__main__":
    main()