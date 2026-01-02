import numpy as np
from pprint import pprint


def solve(MM, H, W):

    L, R, U, D = np.zeros((H, W), dtype=int), np.zeros((H, W), dtype=int), np.zeros((H, W), dtype=int), np.zeros((H, W), dtype=int)

    for i in range(H):
        i_r = H - 1 - i

        # L, U
        for j in range(W):
            j_r = W - 1 - j

            # L
            if MM[i][j]:
                if j == 0:
                    L[i][j] = 1
                else:
                    L[i][j] = L[i][j - 1] + 1

            # R
            if MM[i][j_r]:
                if j_r == W - 1:
                    R[i][j_r] = 1
                else:
                    R[i][j_r] = R[i][j_r + 1] + 1

            # U
            if MM[i][j]:
                if i == 0:
                    U[i][j] = 1
                else:
                    U[i][j] = U[i - 1][j] + 1

            # D
            if MM[i_r][j]:
                if i_r == H - 1:
                    D[i_r][j] = 1
                else:
                    D[i_r][j] = D[i_r + 1][j] + 1

    print((L + R + U + D - 3).max())


def solve2(MM, H, W):
    L, R, U, D = [MM.copy() for _ in range(4)]

    # U, D
    for i in range(1, H):
        U[i] = (U[i - 1] + 1) * MM[i]
        i_r = H - 1 - i
        D[i_r] = (D[i_r + 1] + 1) * MM[i_r]

    MM_T = MM.T
    L_T, R_T = L.T, R.T

    # L, R
    for i in range(1, W):
        L_T[i] = (L_T[i - 1] + 1) * MM_T[i]
        i_r = W - 1 - i
        R_T[i_r] = (R_T[i_r + 1] + 1) * MM_T[i_r]

    L, R = L_T.T, R_T.T
    print((L + R + U + D).max() - 3)


def stdin():
    H, W = [int(x) for x in input().split()]
    MM = np.zeros((H, W), dtype=int)

    for i in range(H):
        line = str(input())

        for j in range(W):
            if line[j] != '#':
                MM[i][j] = 1

    solve2(MM, H, W)


if __name__ == '__main__':
    stdin()
