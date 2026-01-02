import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
input = sys.stdin.buffer.readline

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

# A[i]: iの次の要素
# M: 何個先まで調べたいか
class Doubling(object):
    def __init__(self,A,M):
        self.N = len(A)
        self.kmax = M.bit_length()
        # nex[i][k]: i番目の2^k先
        self.nex = [[-1]*self.kmax for _ in range(N)]
        for i in range(N):
            self.nex[i][0] = A[i]
        
        for k in range(1,self.kmax):
            for i in range(N):
                if self.nex[i][k-1] == -1:
                    self.nex[i][k] = -1
                else:
                    self.nex[i][k] = self.nex[self.nex[i][k-1]][k-1]
    
    # i番目の要素のx個先
    def query(self,i,x):
        for k in range(self.kmax)[::-1]:
            if i == -1:
                break
            if (x >> k) & 1:
                i = self.nex[i][k]
        return i

N,K = LI()
A = LI()
A = list(map(lambda x: x-1, A))

d = Doubling(A,K)
print(d.query(0,K)+1)