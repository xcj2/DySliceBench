import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

class BIT:
    '''
    a[1]~a[n]の数列を想定
    '''

    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def add(self, index, x):
        '''
        a[index]にxを加算
        '''
        while index <= self.size:
            self.tree[index] += x
            index += index & (-index)
 
    def sum(self, index):
        '''
        a[1]~a[index]の和
        '''
        s = 0
        while index:
            s += self.tree[index]
            index -= index & (-index)
        return s
 
    def search(self, value):
        '''
        sum(index)>=value を満たす最小のindex
        sum(n)<value のとき n+1 を返す
        '''
        i = 0
        s = 0
        step = 1 << (self.size.bit_length() - 1)
        while step:
            if i + step <= self.size and s + self.tree[i + step] < value:
                i += step
                s += self.tree[i]
            step //= 2
        return i + 1
        
        
def index_sort(A,reverse=False):
    x = []
    for i,a in enumerate(A):
        x.append((a,i))
    if reverse:
        return sorted(x, key=lambda x: -x[0])
    else:
        return sorted(x, key=lambda x: x[0])

      
N = I()
P = III()

bit = BIT(N)
x = index_sort(P,True)

ans = 0
for i in range(N):
    index = x[i][1]
    if index>=1:
        L = bit.sum(index)
    else:
        L = 0
    wi = bit.search(L-1) if L>=2 else 0
    xi = bit.search(L) if L>=1 else 0

    R = bit.sum(N)-bit.sum(index+1)
    yi = bit.search(L+1)
    zi = bit.search(L+2)

    ci = (xi-wi)*(yi-index-1) + (index+1-xi)*(zi-yi)
    ans += ci*x[i][0]
    bit.add(index+1, 1)

print(ans)