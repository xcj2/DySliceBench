import sys

stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)


def li(): return map(int, stdin.readline().split())


def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())


def lf(): return map(float, stdin.readline().split())


def ls(): return stdin.readline().split()


def ns(): return stdin.readline().rstrip()


def lc(): return list(ns())


def ni(): return int(stdin.readline())


def nf(): return float(stdin.readline())

N = int(input())
P_str = input().split()
P = [int(p) for p in P_str]

Q = sorted(P)
check = 0
for i in range(len(P)):
    if P[i] != Q[i]:
        check += 1

    if check > 2:
        print("NO")
        exit()

if check == 1:
    print("NO")
    exit()

print("YES")

