import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)

    def add(self, i, x=1):
        i += 1
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get_sum(self, i):
        i += 1
        x = 0
        while i > 0:
            x += self.data[i]
            i -= i & -i
        return x

    # Return sum for [l, r)
    def get_sum_range(self, l, r):
        return self.get_sum(r - 1) - self.get_sum(l - 1)


def main():
    N = int(readline())
    S = readline().strip()
    Q = int(readline())

    S = list(S)
    base = ord('a')

    tree = [BIT(N) for _ in range(26)]
    for i, c in enumerate(S):
        tree[ord(c) - base].add(i)

    ans = []
    for _ in range(Q):
        n, a, b = readline().split()
        if n == '1':
            i = int(a) - 1
            if S[i] != b:
                tree[ord(S[i]) - base].add(i, -1)
                tree[ord(b) - base].add(i, 1)
                S[i] = b
        else:
            l, r = int(a) - 1, int(b)
            tmp = 0
            for i in range(26):
                if tree[i].get_sum_range(l, r) > 0:
                    tmp += 1
            ans.append(tmp)

    print('\n'.join(map(str, ans)))
    return


if __name__ == '__main__':
    main()
