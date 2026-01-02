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

    N, K = in_nn()
    A = in_nl()

    def judge(x):

        cnt = 0
        for i in range(N):
            q, r = divmod(A[i], x)
            if r == 0:
                q -= 1
            cnt += q

        return cnt <= K

    def binary_search(min_n, max_n):

        while max_n - min_n != 1:
            mid = (min_n + max_n) // 2
            if judge(mid):
                max_n = mid
            else:
                min_n = mid

        return max_n

    ans = binary_search(min_n=0, max_n=10**9)
    print(ans)


if __name__ == '__main__':
    main()
