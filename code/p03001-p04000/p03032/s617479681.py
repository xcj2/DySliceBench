import sys
sys.setrecursionlimit(10 ** 5)


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def cal(r, k, K, V):
    l = k - r
    if l == 0:
        A = V[:r]
    elif r == 0:
        A = V[-l:]
    else:
        A = V[:r] + V[-l:]
    A.sort()
    for i, a in enumerate(A):
        if i < min(k, K-k) and a < 0:
            A[i] = 0
        else:
            break
    return sum(A)


def main():
    N, K = LI()
    V = LI()
    ans = 0
    for k in range(1, min(N, K)+1):
        for l in range(k+1):
            ans = max(ans, cal(l, k, K, V))
    print(ans)
    return


main()
