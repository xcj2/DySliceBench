import sys
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
class BIT():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.UNITY_SUM = 0
        self.dat = [[self.UNITY_SUM for i in range(n + 1)] for j in range(2)]
    
    def sub_ADD(self, p, a, x):
        i = a
        while i < len(self.dat[p]):
            self.dat[p][i] = self.dat[p][i] + x
            i += i & -i
    
    def ADD(self, a, b, x):
        self.sub_ADD(0, a, x * -(a - 1))
        self.sub_ADD(1, a, x)
        self.sub_ADD(0, b, x * (b - 1))
        self.sub_ADD(1, b, x * (-1))
    
    def sub_SUM(self, p, a):
        res = self.UNITY_SUM
        i = a
        while i > 0:
            res += self.dat[p][i]
            i -= i & -i
        return res
    
    def SUM(self, a, b):
        return self.sub_SUM(0, b - 1) + self.sub_SUM(1, b - 1) * (b - 1) - self.sub_SUM(0, a - 1) - self.sub_SUM(1, a - 1) * (a - 1)
    
    def PRINT(self):
        for i in range(1, len(self.dat[0])):
            print(self.SUM(i, i + 1), end = "")
            print(",", end = "")
        print()
 
def main():
    N, Q = map(int,readline().split())
    C = list(map(int,readline().split()))  #対象のリスト
    S = sys.stdin.readlines()
    lefts = [0] * Q
    rights = [0] * Q
    ids = [0] * Q
    for i in range(Q):
        lefts[i], rights[i] = map(int,S[i].split())
        lefts[i] -= 1
        ids[i] = i
    
    ids = sorted(ids, key=lambda x: rights[x])
 
    bit = BIT(N+5)
    prev = [-1] * 1100000
    res = [0] * Q
    r = 0
    for i in ids:
        while r < rights[i]:
            bit.ADD(prev[C[r]]+2, r+2, 1)
            prev[C[r]] = r
            r += 1
        tmp = bit.SUM(lefts[i]+1, lefts[i]+2)
        res[i] = max(res[i], tmp)
    for i in range(Q):
        print(res[i])
 
main()