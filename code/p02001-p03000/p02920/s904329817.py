from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())


class Node:
    def __init__(self,value,index):
        self.value = value
        self.index = index

    def items(self):
        return [self.value,self.index]

# 0-indexed SegmentTree
class SegmentTree:
    def __init__(self,N,aa):
        self.N0 = 2**(N-1).bit_length()
        self.nodes = [Node(-1,i+1-self.N0) for i in range(2*self.N0-1)]
        for i in reversed(range(2*self.N0-1)):
            ind = i+1-self.N0
            if ind >= N:
                self.nodes[i].value = -1
            elif N > ind >= 0:
                self.nodes[i].value = aa[ind]
            else:
                self.nodes[i] = self.process(self.nodes[i*2+1],self.nodes[i*2+2])

    def update(self,i,x): #iの値をxに更新
        i += self.N0 - 1
        self.nodes[i].value = x
        while i > 0:
            i = (i-1)//2
            self.nodes[i] = self.process(self.nodes[i*2+1],self.nodes[i*2+2])

    def query(self,L,R): #[L,R)の値
        retnode = Node(-1,-1)
        L += self.N0
        R += self.N0
        while L < R:
            if R&1 :
                R -= 1
                retnode = self.process(retnode,self.nodes[R-1])
            if L&1 :
                retnode = self.process(retnode,self.nodes[L-1])
                L += 1
            L >>= 1; R >>= 1
        return retnode

    def process(self,node_x,node_y): #x,yが子の時，親に返る値
        if node_x.value > node_y.value:
            return node_x
        else:
            return node_y


N = inp()
SS = inpl()
SS.sort()

ST = SegmentTree(2**N,SS)

now = [SS[-1]]

Rinds = [0]*(2**N)
itr = 0
for i,S in enumerate(SS):
    while True:
        if S <= SS[itr]:
            Rinds[i] = itr
            break
        else:
            itr += 1


now = [Node(SS[2**N-1],2**N-1)]

for t in range(1,N+1):
    next = []
    for n in now:
        R = Rinds[n.index]
        tmpnode = ST.query(0,R)
        if tmpnode.value < 0:
            print('No')
            exit()
        next.append(tmpnode)
        ST.update(tmpnode.index,-1)

    now = now + next


print('Yes')
