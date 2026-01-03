import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    md = 10 ** 9 + 7
    n = int(input())
    s1 = input()
    s2 = input()
    if s1[0] == s2[0]:
        ans = 3
        pre = 0
        i = 1
    else:
        ans = 6
        pre = 1
        i = 2
    while i < n:
        if s1[i] == s2[i]:
            if pre == 0:
                ans *= 2
            pre = 0
            i += 1
        else:
            if pre == 0:
                ans *= 2
            else:
                ans *= 3
            pre = 1
            i += 2
        ans %= md
    print(ans)

main()
