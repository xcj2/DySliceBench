import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def solve():
    ans = -inf
    for si in range(n):
        cs = [0]
        i = si
        for _ in range(k):
            i = pp[i]
            cs.append(cs[-1] + cc[i])
            if i == si: break
        cur = max(cs[1:])
        if len(cs) < k + 1:
            d = len(cs) - 1
            c = k // d
            r = k - d * c
            cur1=cs[-1] * c + max(cs[:r+1])
            cur2=cs[-1]*(c-1)+max(cs)
            cur = max(cur,cur1,cur2)
        #print(cs)
        ans = max(ans, cur)
    print(ans)

inf=10**16
n,k=MI()
pp=LI1()
cc=LI()
solve()
