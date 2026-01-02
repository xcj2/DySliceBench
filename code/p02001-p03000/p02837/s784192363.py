import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    def check(s):
        for i in range(n):
            if s>>i & 1:
                for j, y in to[i]:
                    if s >> j & 1 != y:
                        return False
        return True

    to = defaultdict(list)
    n = int(input())
    for i in range(n):
        a = int(input())
        for _ in range(a):
            x, y = MI()
            to[i].append([x - 1, y])
    ans = 0
    for s in range(1 << n):
        if check(s):
            ans = max(ans, bin(s).count("1"))
    print(ans)

main()
