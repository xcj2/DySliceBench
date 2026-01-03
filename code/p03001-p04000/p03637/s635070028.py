import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    n = int(input())
    aa = LI()
    c4 = c2 = 0
    for a in aa:
        if a % 4 == 0:
            c4 += 1
        elif a % 2 == 0:
            c2 += 1
    max_len = 0
    if c4 > 0 and c2 > 1:
        max_len = c4 * 2 + c2
    elif c4 > 0:
        max_len = c4 * 2 + 1
    elif c2 > 1:
        max_len = c2
    if n <= max_len:
        print("Yes")
    else:
        print("No")

main()
