import sys

# Set max recursion limit
sys.setrecursionlimit(1000000)


def li_input():
    return [int(_) for _ in input().split()]


def is_boardable(W, P, K):
    T = [0] * K

    wi = 0
    ti = 0
    while wi < len(W):
        if T[ti] + W[wi] <= P:
            T[ti] += W[wi]
            wi += 1
        else:
            ti += 1

            if ti == K:
                return False
    
    return True


def main():
    N, K = li_input()
    W = [int(input()) for _ in range(N)]

    l = 0
    r = 100000 * 10000

    while l + 1 < r:
        m = (l + r) // 2

        if is_boardable(W, m, K):
            P = m
            r = m
        else:
            l = m

    print(P)
    

main()

