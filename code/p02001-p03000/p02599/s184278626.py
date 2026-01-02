def main():
    import sys
    input = sys.stdin.readline
    class BIT:
        def __init__(self,n):
            self.size = n
            self.tree = [0]*(n+1)

        def add(self,i,x):
            while i <= self.size:
                self.tree[i] += x
                i += i&-i

        def sum(self,i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i&-i
            return s

    N,Q = map(int,input().split())
    C = list(map(int,input().split()))
    LR = []
    for i in range(Q):
        l,r = map(int,input().split())
        LR.append((l,r,i))
    bit = BIT(N)
    #color[i] => 色iが最後に登場したインデックス(1-indexed)
    color = [0]*(N+1)

    ANS = [0]*Q
    LR.sort(key=lambda x: x[1])
    cur = 1
    for l,r,j in LR:
        for i in range(cur,r+1):
            c = C[i-1]
            if color[c] != 0:
                bit.add(color[c],-1)
            color[c] = i
            bit.add(i,1)
        cur = r+1
        ANS[j] = bit.sum(r)-bit.sum(l-1)
    for a in ANS:
        print(a)
main()