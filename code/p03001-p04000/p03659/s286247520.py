def main():
    N = int(input())
    A = list(map(int, input().split()))

    solve(N,A)

def solve(N,A):
    ans = float("inf")

    # ans = TLE(N,A,ans)
    ans = AC(N,A,ans)

    print(ans)

def TLE(N,A, ans):
    for i in range(1, N):
        snk = sum(A[:i])
        ari = sum(A[i:])

        ans = min(ans, abs(snk - ari))

    return ans

def AC(N,A,ans):
    cum_A = [None] * N
    cum_A[0] = A[0]
    for i in range(1, N):
        cum_A[i] = cum_A[i-1] + A[i]

    for i in range(N-1):
        snk = cum_A[i]
        ari = cum_A[-1] - snk

        ans = min(ans, abs(snk - ari))

    return ans

if __name__ == "__main__":
    main()
