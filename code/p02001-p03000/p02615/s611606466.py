import sys
sys.setrecursionlimit(10**8)
stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N = ni()

a_array = na()

a_array.sort(reverse=True)

ans = a_array[0]

idx = 1

depth = 1

start = 1
end = 2

while(N - 1 > idx):
    start = 2 ** (depth-1)
    end = 2 ** depth
    if idx + 2 ** depth < N:
        ans += sum(a_array[start:end]) * 2
        idx = idx + 2 ** depth
    else:
        rest = (N - 1) - idx
        ans += sum(a_array[start:(start+rest//2)]) * 2
        ans += (rest % 2) * a_array[start+rest//2]
        idx = N - 1
    depth += 1
    # print(idx, ans)


print(ans)
