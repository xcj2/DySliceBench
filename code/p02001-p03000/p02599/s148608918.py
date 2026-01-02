class BIT: # 1Indexed
    def __init__(self,size):
        self.array = [0]*size
        self.size  = size
    def add(self,ind,value):
        while ind <= self.size:
            self.array[ind-1] += value
            ind += ind & -ind
    def sum(self,x):
        out = 0
        while x > 0:
            out += self.array[x-1]
            x -= x & -x
        return out

################### ABC174F ###################

import sys
input = sys.stdin.readline

def main(N,Q,c,q):
    bit = BIT(N)
    rbi= {}
    ans = [0]*Q
    q.sort(key= lambda x:x[1])
    R = 0
    for l,r,ind in q:
        for i in range(R,r):
            if c[i] in rbi:
                bit.add(rbi[c[i]],-1)
            rbi[c[i]] = i+1
            bit.add(rbi[c[i]],1)
        ans[ind] = bit.sum(r)-bit.sum(l-1)
        R = r
    return ans

if __name__ == "__main__":
    N,Q = map(int,input().split())
    c = list(map(int,input().split()))
    q = list( list(map(int,input().split()))+[i] for i in range(Q))
    ans = main(N,Q,c,q)
    for i in ans:
        print(i)