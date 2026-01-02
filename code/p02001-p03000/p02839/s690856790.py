import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


H, W = na()
A_array = naa(H)
B_array = naa(H)
C_array = [[abs(aa-bb) for aa, bb in zip(a, b)]
           for a, b in zip(A_array, B_array)]
# print(C_array)

K = 6400

ans_array = [[[0] * (K+1) for _ in range(W)] for _ in range(H)]

ans_array[0][0][C_array[0][0]] = 1

for i in range(H):
    for j in range(W):
        if i != 0:
            for k in range(K+1):
                ans_array[i][j][k] = ans_array[i][j][k] | ((ans_array[i-1][j][abs(k+C_array[i][j])] if abs(
                    k+C_array[i][j]) <= K else 0) | ans_array[i-1][j][abs(k-C_array[i][j])])
        if j != 0:
            for k in range(K+1):
                ans_array[i][j][k] = ans_array[i][j][k] | ((ans_array[i][j-1][abs(k+C_array[i][j])] if abs(
                    k+C_array[i][j]) <= K else 0) | ans_array[i][j-1][abs(k-C_array[i][j])])

# print(ans_array)

for k in range(K+1):
    if ans_array[H-1][W-1][k] == 1:
        print(k)
        exit()
