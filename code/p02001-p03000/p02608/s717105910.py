import sys
sys.setrecursionlimit(10**8)
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N = ni()

ans_array = [0] * (N+1)

for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            d = x * x + y * y + z * z + x * y + y * z + z * x
            if d <= N:
                ans_array[d] += 1


for i in range(N):
    print(ans_array[i+1])
