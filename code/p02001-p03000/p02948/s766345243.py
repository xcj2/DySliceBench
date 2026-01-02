import sys
sys.setrecursionlimit(10**7) #再帰関数の上限,10**5以上の場合python
import math
from copy import copy, deepcopy
from copy import deepcopy as dcp
from operator import itemgetter
from bisect import bisect_left, bisect, bisect_right#2分探索
#bisect_left(l,x), bisect(l,x)#aはソート済みである必要あり。aの中からx未満の要素数を返す。rightだと以下
from collections import deque
#deque(l), pop(), append(x), popleft(), appendleft(x)
#q.rotate(n)で → にn回ローテート
from collections import Counter#文字列を個数カウント辞書に、
#S=Counter(l),S.most_common(x),S.keys(),S.values(),S.items()
from itertools import accumulate,combinations,permutations#累積和
#list(accumulate(l))
from heapq import heapify,heappop,heappush
#heapify(q),heappush(q,a),heappop(q) #q=heapify(q)としないこと、返り値はNone
#import fractions#古いatcoderコンテストの場合GCDなどはここからimportする
from functools import lru_cache#pypyでもうごく
#@lru_cache(maxsize = None)#maxsizeは保存するデータ数の最大値、2**nが最も高効率
from decimal import Decimal

def input(): 
    x=sys.stdin.readline()
    return x[:-1] if x[-1]=="\n" else x
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
class BIT():#添字は1から始まることに注意
    def __init__(self, max_n):
        self.size = max_n + 1
        self.tree = [0] * self.size
        self.depth = self.size.bit_length()
        
    def initialize(self,seq):
        tree = self.tree
        size = self.size
        for i,x in enumerate(seq,1):
            tree[i] += x
            j = i+(i&(-i))
            if j < size:
                tree[j] += tree[i]
        
    def __repr__(self):
        return self.tree.__repr__()
        
    def get_sum(self,i):
        tree = self.tree
        s = 0
        while i:
            s += tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        tree = self.tree
        size = self.size
        while i < size:
            tree[i] += x
            i += i & -i
    
    def find_kth_element(self,k):#k番目（最小は１）の要素
        tree = self.tree; size = self.size
        x,sx = 0,0
        dx = 1 << (self.depth)
        for i in range(self.depth - 1, -1, -1):
            dx = (1 << i)
            if x + dx >= size:
                continue
            y = x + dx
            sy = sx + tree[y]
            if sy < k:
                x,sx = y,sy
        return x + 1
 
def main():
    mod = 1000000007
    #w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    #N = int(input())
    N, M = map(int, input().split())
    #A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    S = list(tuple(map(int, input().split())) for i in range(N)) #改行行列
    S.sort(key=itemgetter(1),reverse=True)
    #print(S)
    ans=0
    fil=[1 for i in range(M)]

    tot=M
    bit=BIT(M)
    bit.initialize(fil)
    for s in S:
        a,b=s
        if a>M:continue
        #print(tot,tot-bit.get_sum(a-1),M+1-a)
        
        #print(a-1,M)
        t=bit.get_sum(a-1)
        #print(t,tot)
        if t>=tot:
            continue

        x=bit.find_kth_element(t+1)
        
        bit.add(x,-1)
        ans+=b
        tot-=1

    print(ans)
    


        




if __name__ == "__main__":
    main()