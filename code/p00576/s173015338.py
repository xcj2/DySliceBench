import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n = int(input())
    xx = LI()
    m = int(input())
    aa = LI()
    line = [0] * 2020
    pos = [-1] * (n + 1)
    for a, x in enumerate(xx, 1):
        line[x] = a
        pos[a] = x
    for a in aa:
        if pos[a]==2019 or line[pos[a] + 1] != 0: continue
        line[pos[a]] = 0
        line[pos[a] + 1] = a
        pos[a] += 1
    for x in pos[1:]:
        print(x)

main()

