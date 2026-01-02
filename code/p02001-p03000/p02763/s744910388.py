import bisect
import math
from collections import deque

def sRaw():
    return input().rstrip("\r")


def iRaw():
    return int(input())


def ssRaw():
    return input().split()


def isRaw():
    return list(map(int, ssRaw()))

INF = 1 << 29

class Node:
    def __init__(self, val, idx=0):
        self.val = val
        self.idx = idx

    def __str__(self):
        return 'val : ' + str(self.val) + ' idx : ' + str(self.idx)

# 0-idxed SegmentTree
class SegmentTree:
    def __init__(self, N, vals, default_value=INF):
        self.N0 = pow(2, (N-1).bit_length())
        self.nodes = [Node(default_value, i+1-self.N0)
                      for i in range(2*self.N0-1)]
        for i in reversed(range(2*self.N0-1)):
            ind = i+1-self.N0
            if ind >= N:
                self.nodes[i].val = default_value
            elif ind >=0 and N > ind:
                self.nodes[i].val = vals[ind]
            else:
                self.nodes[i] = self.propagate(
                    self.nodes[i*2+1], self.nodes[i*2+2])

    def __getitem__(self, key):  # getiten : ST[i]
        return self.nodes[key+self.N0-1].val

    def __setitem__(self, i, x):  # update : ST[i] = x
        i += self.N0 - 1
        self.nodes[i].val = x
        while i > 0:
            i = (i-1)//2
            self.nodes[i] = self.propagate(self.nodes[i*2+1], self.nodes[i*2+2])

    def __str__(self):
        return '['+', '.join(map(str, [self.nodes[i+self.N0-1].val for i in range(self.N0)]))+']'

    def query(self, L, R):  #value of [L,R)
        retnode = Node(0, 0)
        L += self.N0
        R += self.N0
        while L < R:
            if R & 1:
                R -= 1
                retnode = self.propagate(retnode, self.nodes[R-1])
            if L & 1:
                retnode = self.propagate(retnode, self.nodes[L-1])
                L += 1
            L >>= 1
            R >>= 1
        return retnode

    def propagate(self, node_x, node_y):  # return parent if x,y is child
        return Node(node_x.val | node_y.val)


def main():
    N = iRaw()
    S = sRaw()
    sgt = SegmentTree(N, [1 << (ord(s)-ord('a')) for s in S])
    Q = iRaw()
    ans =[]
    for _ in range(Q):
        t,l,r = ssRaw()
        if t=="1":
            sgt[int(l)-1] = 1 << (ord(r)-ord("a"))
        else:
            ret = sgt.query(int(l)-1, int(r))
            ans.append(str(bin(ret.val)).count("1"))
    return "\n".join(map(str, ans))

if __name__ == "__main__":
    print(main())
