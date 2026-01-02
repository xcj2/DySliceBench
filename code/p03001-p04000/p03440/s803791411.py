import sys
sys.setrecursionlimit(10**7) #再帰関数の上限,10**5以上の場合python
import math
from copy import copy, deepcopy
from operator import itemgetter
from bisect import bisect_left, bisect, bisect_right#2分探索
#bisect_left(l,x), bisect(l,x)#aはソート済みである必要あり。aの中からx未満の要素数を返す。rightだと以下
from collections import deque
#deque(l), pop(), append(x), popleft(), appendleft(x)
##listでqueの代用をするとO(N)の計算量がかかってしまうので注意
from collections import Counter#文字列を個数カウント辞書に、
#S=Counter(l),S.most_common(x),S.keys(),S.values(),S.items()
from itertools import accumulate#累積和
#list(accumulate(l))
from heapq import heapify,heappop,heappush
#heapify(q),heappush(q,a),heappop(q) #q=heapify(q)としないこと、返り値はNone
#import fractions#古いatcoderコンテストの場合GCDなどはここからimportする
from functools import lru_cache#pypyでもうごく
#@lru_cache(maxsize = None)#maxsizeは保存するデータ数の最大値、2**nが最も高効率

def input(): return sys.stdin.readline()[:-1]
def printl(li): print(*li, sep="\n")
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


class UnionFind:#早いunionfind,親はclass[i]のように要素指定すればok
    def __init__(self, elements=None):
        """Create a new empty union-find structure.
        If *elements* is an iterable, this structure will be initialized
        with the discrete partition on the given set of elements.
        """
        if elements is None:
            elements = ()
        self.parents = {}
        self.weights = {}
        for x in elements:
            self.weights[x] = 1
            self.parents[x] = x

    def __getitem__(self, i):
        """Find and return the name of the set containing the i."""

        # check for previously unknown i
        if i not in self.parents:
            self.parents[i] = i
            self.weights[i] = 1
            return i

        # find path of is leading to the root
        path = [i]
        root = self.parents[i]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def __iter__(self):#for parent in Class:
        return iter(self.parents)

    def union(self, *objects):#union the parents of objects
        """Find the sets containing the objects and merge them all."""
        roots = [self[x] for x in objects]
        # Find the heaviest root according to its weight.
        heaviest = max(roots, key=lambda r: self.weights[r])
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest

    def __len__(self):
        return len(self.parents)


def main():
    mod = 10**9+7
    #w.sort(key=itemgetter(1),reversed=True)  #二個目の要素で降順並び替え

    #N = int(input())
    N, M = map(int, input().split())
    A = tuple(map(int, input().split())) #1行ベクトル
    #L = tuple(int(input()) for i in range(N)) #改行ベクトル
    #S = tuple(tuple(map(int, input().split())) for i in range(N)) #改行行列
    tree=UnionFind(list(range(N)))
    for i in range(M):
        x,y=map(int, input().split())
        tree.union(x,y)
    d=dict()
    for i in range(N):
        root=tree[i]
        if root not in d:
            d[root]=[]
        heappush(d[root],A[i])
    nr=len(d.keys())
    if nr==1:
        print(0)
        return

    if 2*(nr-1)>N:
        print('Impossible')
        return 
    
    ans=0
    #print(d)
    ocount=0
    As=[]
    
    for j, q in d.items():
        a=heappop(q)
        ans+=a
        As+=q
    
    As.sort()
    for i in range(0,nr-2):
        ans+=As[i]
    


    print(ans)

    






if __name__ == "__main__":
    main()