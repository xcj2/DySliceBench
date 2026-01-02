FREE = -1
NOT_FREE = 1

N = 8
B = [["."] * N for _ in range(N)]
row = [FREE] * N
col = [FREE] * N
dpos = [FREE] * (2 * N - 1)
dneg = [FREE] * (2 * N - 1)

def update(r, c, FREE_OR_NOT):
    B[r][c] = "." if FREE_OR_NOT == FREE else "Q"
    row[r] = col[c] = dpos[r + c] = dneg[r - c + N - 1] = FREE_OR_NOT

def draw():
    for i in range(N):
        print("".join(B[i]))

def recursive(i):
    if i == N:
        draw()
        return
    if "Q" in B[i]:
        recursive(i + 1)

    for j in range(N):
        if NOT_FREE in [row[i], col[j], dpos[i + j], dneg[i - j + N - 1]]:
            continue
        else:
            update(i, j, NOT_FREE)
        recursive(i + 1)
        update(i, j, FREE)

k = int(input())

for _ in range(k):
    r, c = map(int, input().split())
    update(r, c, NOT_FREE)
recursive(0)
