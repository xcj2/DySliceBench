import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

class BitSum:
    def __init__(self, n):
        self.n = n + 1
        self.table = [0] * self.n

    def add(self, i, x):
        i += 1
        while i < self.n:
            self.table[i] += x
            i += i & -i

    def sum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.table[i]
            i -= i & -i
        return res

def main():
    md=998244353
    n=II()
    xy=LLI(n)
    yy=set()
    for x,y in xy:yy.add(y)
    ytoj={y:j for j,y in enumerate(sorted(yy))}

    ans=n*(pow(2,n,md)-1)-4*(pow(2,n,md)-1-n)
    ans%=md

    xy.sort()
    bit=BitSum(200005)
    for i,[x,y] in enumerate(xy):
        j=ytoj[y]
        c=bit.sum(j-1)
        ans+=pow(2,c,md)-1
        ans+=pow(2,i-c,md)-1
        ans%=md
        bit.add(j,1)

    bit=BitSum(200005)
    for i,[x,y] in enumerate(xy[::-1]):
        j=ytoj[y]
        c=bit.sum(j-1)
        ans+=pow(2,c,md)-1
        ans+=pow(2,i-c,md)-1
        ans%=md
        bit.add(j,1)

    print(ans)

main()