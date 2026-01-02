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
    query = [readline().split() for _ in range(Q)]

    bit = [BIT(N) for _ in range(26)]
    for i, c in enumerate(S):
        bit[ord(c) - ord('a')].add(i)

    S = list(S)
    ans = []

    for q in query:
        if q[0] == '1':
            i = int(q[1]) - 1
            c = q[2]
            bit[ord(S[i]) - ord('a')].add(i, -1)
            bit[ord(c) - ord('a')].add(i, 1)
            S[i] = c
        else:
            res = 0
            l, r = int(q[1]) - 1, int(q[2]) - 1
            for i in range(26):
                if bit[i].get_sum_range(l, r + 1):
                    res += 1
            ans.append(res)

    print(*ans, sep='\n')

    return


if __name__ == '__main__':
    main()
