import sys

def I(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))

def main():
    N = I()
    a = LI()
    t = [0, 0, 0]
    for ai in a:
        t[ai-1] += 1
    A, B, C = t
    E = B+C

    dp = [[0 if (i+j==0) else N/(i+j) for j in range(E+1)] for i in range(N+1)]

    for k in range(C+1):
        for i in range(N+1):
            dp[i][E] = 0 if (i+E+k==0) else N/(i+E+k)
        for j in range(E+1):
            for i in range(N+1):
                z = i+j+k
                if (not z):
                    continue
                d = dp[i][j]
                if (i<N):
                    dp[i+1][j] += (i+1)*d/(z+1)
                if (i>0) and (j<E):
                    dp[i-1][j+1] += (j+1)*d/z
                if (j>0) and (k<C):
                    dp[i][j-1] = (k+1)*d/z + N/z

    print(dp[A][B])

if __name__ == "__main__":
    main()
