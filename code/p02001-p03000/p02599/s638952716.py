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

    N, Q = in_nn()
    C = in_nl()
    LR = []

    for q in range(Q):
        l, r = in_nn()
        LR.append((r + 0.1, l, q))

    t = [-1] * (N + 1)
    sect = []
    for i in range(N):
        x = C[i]
        if t[x] != -1:
            sect.append((i + 1, t[x], -1))
        t[x] = i + 1

    sect += LR
    sort_index = sorted(list(range(len(sect))), key=lambda i: sect[i][0])

    bit = [0] * (N + 1)

    def add(i, val):
        while i <= N:
            bit[i] += val
            i += i & -i

    def sum(i):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i & -i
        return res

    ans = [0] * Q
    for i in sort_index:
        r, l, n = sect[i]
        r = int(r)

        if n == -1:
            add(l, 1)
        else:
            t = sum(r) - sum(l - 1)
            ans[n] = r - l + 1 - t

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
