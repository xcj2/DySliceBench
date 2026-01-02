def main():
    import sys
    input = sys.stdin.readline
    from collections import Counter
    class BIT:
        def __init__(self,n):
            self.size = n
            self.tree = [Counter([]) for _ in range(n+1)]
    
        def change(self,i,x,y):
            while i <= self.size:
                if x in self.tree[i]:
                    self.tree[i][x] -= 1
                if y not in self.tree[i]:
                    self.tree[i][y] = 0
                self.tree[i][y] += 1
                i += i&-i
    
        def sum(self,i):
            res = Counter([])
            while i > 0:
                res += self.tree[i]
                i -= i&-i
            return res

    N = int(input())
    st = BIT(N)
    S = list(input())
    Q = int(input())
    for i in range(N):
        st.change(i+1," ",S[i])

    for _ in range(Q):
        q,a,b = input().split()
        if q == "1":
            st.change(int(a),S[int(a)-1],b)
            S[int(a)-1] = b
        else:
            res = st.sum(int(b)) - st.sum(int(a)-1)
            ans = 0
            for v in res.values():
                if v > 0:
                    ans += 1
            print(ans)
main()
