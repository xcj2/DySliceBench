
class BIT:
    """Binary Indexed Tree (Fenwick Tree)
    Range Sum QueryにO(log N)時間で答える
    1-indexed
    """
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()
 
    def sum(self, i):
        """a[1]~a[i]の区間和を取得"""
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        """a[i]にxを足す"""
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += 1 << i
        return pos + 1, sum_
 
def main():
    N = int(input())
    S = list(input())
    Q = int(input())
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    c2n = {c: i for i, c in enumerate(alphabets)}
    
    Trees = [BIT(N+2) for _ in range(26)]

    for i in range(N):
        Trees[c2n[S[i]]].add(i+1, 1)
    
    for _ in range(Q):
        tmp = list(input().split())
        if tmp[0] == "1":
            _, i, c = tmp
            i = int(i)
            Trees[c2n[S[i-1]]].add(i, -1)
            Trees[c2n[c]].add(i, 1)
            S[i-1] = c
        else:
            ans = 0
            _, l, r = tmp
            l = int(l)
            r = int(r)
            for char in range(26):
                if Trees[char].sum(r) - Trees[char].sum(l-1) > 0:
                    ans += 1
            print(ans)

if __name__ == "__main__":
    main()