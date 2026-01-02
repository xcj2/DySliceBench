class BIT:
    def __init__(self, N):
        self.tree = [0] * (N + 1)  # 1-indexed
        self.N = N

    def add(self, i, x):
        """tree[i]と関連個所にxを加える"""
        tree = self.tree
        N = self.N
        while i <= N:
            tree[i] += x
            i += i & (-i)

    def sum(self, i):
        tree = self.tree
        s = 0
        while i:
            s += tree[i]
            i -= i & (-i)
        return s


def main():
    from string import ascii_lowercase
    import sys
    input = sys.stdin.readline

    N = int(input())
    s = input().rstrip()
    Q = int(input())

    conv = {c: i for i, c in enumerate(ascii_lowercase)}
    s = [conv[c] for c in s]

    bs = [BIT(N) for _ in range(26)]
    for i, c in enumerate(s, 1):
        bs[c].add(i, 1)

    ans = []
    for _ in range(Q):
        it = iter(input().split())
        if next(it) == '1':
            # change
            i = int(next(it))  # 1-indexed
            c = conv[next(it)]

            p = s[i - 1]
            bs[p].add(i, -1)

            s[i - 1] = c
            bs[c].add(i, 1)

        else:
            # count
            l, r = map(int, it)
            cnt = 0
            for b in bs:
                cnt += int(b.sum(r) - b.sum(l - 1) > 0)
            ans.append(cnt)
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
