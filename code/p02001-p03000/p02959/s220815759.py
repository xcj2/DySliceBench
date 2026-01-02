
import sys

def debug(*args):
    print(*args, file=sys.stderr)


def solve(N, A, B):
    B = B

    result = 0
    for i in range(0, N):
        r0 = min(A[i], B[i])
        A[i] -= r0
        B[i] -= r0
        result += r0
        debug("i=%d"%i, r0)
        if B[i] > 0:
            r = min(A[i+1], B[i])
            A[i+1] -= r
            B[i] -= r
            result += r
            debug("i=%d"%i, r)

    return result


def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    print(solve(N, A, B))

main()
