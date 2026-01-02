import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    def dot(aa, bb):
        return [[sum(a * b for a, b in zip(ar, bc)) % md for bc in zip(*bb)] for ar in aa]

    md = 10 ** 9 + 7
    n, k = MI()
    aa = LLI(n)
    ans=[[(i==j)*1 for j in range(n)] for i in range(n)]
    while k:
        if k & 1:
            ans = dot(ans, aa)
        aa = dot(aa, aa)
        k >>= 1
    # print(ans)
    print(sum(sum(ar) for ar in ans) % md)

main()
