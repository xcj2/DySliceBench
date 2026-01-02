
def debug(*args):
    import sys
    print(*args, file=sys.stderr)

def solve(N, L):
    A = [0] * N
    for i in range(1, N+1):
        A[i-1] = L+i-1

    m = float("inf")
    debug(A)
    for i in range(0, N):
        res = sum(A[:i]) + sum(A[i+1:])
        t = abs(sum(A) - sum(A[:i]) - sum(A[i+1:]))
        #debug("i=%d"%i, "t=%d"%t, A[i], A[:i], A[i+1:], "res:%d"%res)
        if t < m:
            m = t
            ans = sum(A[:i]) + sum(A[i+1:])
    return ans

def main():
    N, L = [int(x) for x in input().split()]
    print(solve(N, L))

main()

