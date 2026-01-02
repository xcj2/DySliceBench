import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():

    N, M, V, P = in_nn()
    A = sorted(in_nl())[::-1]

    # print(A)

    def is_ok(i):
        if i < P:
            return True
        else:
            baf = 0
            for j in range(N):
                if j < P - 1 or i <= j:
                    baf += M
                    continue

                if A[i] + M - A[j] < 0:
                    return False
                else:
                    baf += A[i] + M - A[j]

            # print(i, baf, V * M)
            return V * M <= baf

    def bisect(ng, ok):

        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    ans = bisect(N, 0) + 1
    print(ans)


if __name__ == '__main__':
    main()
