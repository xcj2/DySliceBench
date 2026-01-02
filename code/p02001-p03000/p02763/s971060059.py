"""
セグメント木で行きたいところだけど、集合の管理が必要になるため、時間がかかりすぎてしまう。
と思いきや、文字の種類は26種類しかないので、問題ない。
"""
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
                    self.tree[i][y] = 1
                else:
                    self.tree[i][y] += 1
                i += i&-i
    
        def sum(self,i):
            s = Counter([])
            while i > 0:
                s += self.tree[i]
                i -= i&-i
            cnt = 0
            return s


    N = int(input())
    S = list(input())
    Q = int(input())
    bit = BIT(N)
    for i in range(N):
        bit.change(i+1," ",S[i])

    for _ in range(Q):
        q,a,b = input().split()
        if q == "1":
            x = S[int(a)-1]
            S[int(a)-1] = b
            bit.change(int(a),x,b)
        else:
            a = int(a)
            b = int(b)
            count = bit.sum(b) - bit.sum(a-1)
            ans = 0
            for v in count.values():
                if v > 0:
                    ans += 1
            print(ans)
main()
