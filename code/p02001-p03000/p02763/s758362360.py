import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
# @lru_cache(maxsize=None)
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp():
    '''
    一つの整数
    '''
    return int(input())
def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))

class SegmentTree():
    def __init__(self, init_val, N):
        """
        Parameters
        ----------
        init_val:int
            identity element
        N:int
            the number of nodes
        """
        self.init_val=init_val
        # Range Minimum Query
        self.N0 = 2**(N-1).bit_length() #Nを超える最小の2のべき乗
        # 0-indexedで管理(N0-1からはじまる)
        self.data = [self.init_val] * (2 * self.N0)

    def _segfunc(self, left, right):
        res= left | right
        return res

    def update(self,k, x):
        """
        Parameters
        ----------
        k:int
            target index(0-index)
        x:any
            target value
        """
        k += self.N0-1
        self.data[k] = x
        while k > 0:
            k = (k - 1) // 2
            self.data[k] = self._segfunc(self.data[2*k+1], self.data[2*k+2])

    def query(self, l, r):
        """
        Parameters
        ----------
        l,r:int
            target range [l,r)

        Return
        ----------
        res:any
            val
        """
        L = l + self.N0
        R = r + self.N0
        s = self.init_val
        while L < R:
            if R & 1:
                R -= 1
                s = self._segfunc(s, self.data[R-1])
    
            if L & 1:
                s = self._segfunc(s, self.data[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s

def chartobit(c):
    return 1<<(ord(c)-97)
n=inp()
s=[chartobit(i) for i in list(input()) if i!="\n"]
st = SegmentTree(0, n)
for i in range(n):
    st.update(i,s[i])
q = inp()
ans = []
for i in range(q):
    mode, first, second = input().split()
    if mode == "1":
        # if second in st.data[int(first) - 1 + st.N0 - 1]:
        #     continue
        st.update(int(first) - 1, chartobit(second))
    else:
        ans.append((st.query(int(first) - 1, int(second))))
for i in ans:
    print(sum(map(int,bin(i)[2:])))