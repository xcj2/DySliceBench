import sys
input = sys.stdin.readline

MOD = 998244353
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            self.tree[i] %= MOD
            i += i & -i

def main():
    n, k = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(k)]
    bit = Bit(n + 1)
    bit.add(1, 1)
    for i in range(2, n + 2):
        for l, r in lr:
            plus = bit.sum(i - l) - bit.sum(i - r - 1)
            bit.add(i, plus)
    
    print((bit.sum(n) - bit.sum(n - 1)) % MOD)
    
main()