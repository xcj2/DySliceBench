import sys
sys.setrecursionlimit(10**8)
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


H, W, K = na()

c_array = [ns() for _ in range(H)]

ans = 0
for i in range(2**(H+W)):
    cnt = 0
    for h in range(H):
        for w in range(W):
            if i & (1 << h) == 0 and i & (1 << (H+w)) == 0 and c_array[h][w] == "#":
                cnt += 1
    if cnt == K:
        ans += 1


print(ans)
