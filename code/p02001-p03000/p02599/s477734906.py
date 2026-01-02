def main():
    import sys
    input = sys.stdin.readline
    class BIT:
        def __init__(self,n):
            self.tree = [0]*(n+1)
            self.size = n
        
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
    bit = BIT(N)
    C = list(map(int,input().split()))
    query = []
    for i in range(Q):
        l,r = map(int,input().split())
        query.append([l,r,i])
    query.sort(key=lambda x: x[1])
    ans = [0]*Q
    #良い玉のindexを1-indexで管理する
    colorMemo = [0]*(N+1)
    cur = 1
    for q in query:
        l,r,j = q
        #良い玉の情報を更新する
        for i in range(cur,r+1):
            c = C[i-1]
            if colorMemo[c]:
                bit.add(colorMemo[c],-1)
            bit.add(i,1)
            colorMemo[c] = i
        cur = r + 1
        ans[j]=bit.sum(r)-bit.sum(l-1)

    for a in ans:
        print(a)
main()