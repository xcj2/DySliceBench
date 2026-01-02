import sys,os
from collections import defaultdict, deque
from math import ceil, floor
if sys.version_info[1] >= 5:
    from math import gcd
else:
    from fractions import gcd
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
def main(given=sys.stdin.readline):
    input = lambda: given().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    MOD = 10**9+7

    N,M = LMIIS()
    tree = UnionFind(N)
    P = LMIIS()
    for i in range(M):
        x,y = LMIIS()
        tree.union(x-1,y-1)
    ans = 0
    for i in range(N):
        if i+1 == P[i] or tree.find(i) == tree.find(P[i]-1):
            ans += 1
    print(ans)



    

if __name__ == '__main__':
    main()