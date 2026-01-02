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

    tree = [BIT(N) for _ in range(26)]
    for i, c in enumerate(S):
        tree[ord(c) - ord('a')].add(i)

    ans = []
    for _ in range(Q):
        A = readline().split()
        if A[0] == '1':
            i, c = int(A[1]) - 1, A[2]
            if S[i] != c:
                tree[ord(S[i]) - ord('a')].add(i, -1)
                tree[ord(A[2]) - ord('a')].add(i, 1)
                S[i] = c
        else:
            l, r = int(A[1]) - 1, int(A[2]) - 1
            tmp = 0
            for i in range(26):
                if tree[i].get_sum_range(l, r + 1) > 0:
                    tmp += 1
            ans.append(tmp)

    print('\n'.join(map(str, ans)))
    return


if __name__ == '__main__':
    main()
