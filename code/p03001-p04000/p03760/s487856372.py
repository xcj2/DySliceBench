import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    s0 = SI()
    s1 = SI()
    ans = [""] * (len(s0) + len(s1))
    for i in range(len(s0)):
        ans[i * 2] = s0[i]
    for i in range(len(s1)):
        ans[i * 2 + 1] = s1[i]
    print("".join(ans))

main()
