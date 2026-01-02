class BIT:

    def __init__(self, N):
        # NOTE: 1-indexed
        self.N = N
        self.data = [0] * (N + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & (- i)
        return s

    def update(self, i, x):
        while i <= self.N:
            self.data[i] += x
            i += i & (- i)


def c2n(c):
    return ord(c) - ord('a')


def main():
    N = int(input())
    S = input()
    char_list = list(S)
    trees = [BIT(N) for _ in range(26)]
    for i, c in enumerate(S):
        trees[c2n(c)].update(i + 1, 1)
    Q = int(input())
    ans = list()
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            _, i, c = query
            i = int(i) - 1
            before_c = char_list[i]
            char_list[i] = c
            trees[c2n(before_c)].update(i + 1, - 1)
            trees[c2n(c)].update(i + 1, 1)
        else:  # type '2'
            _, left, right = query
            left, right = int(left) - 1, int(right) - 1
            cnt = 0
            for i in range(26):
                n = trees[i].sum(right + 1) - trees[i].sum(left)
                if n > 0:
                    cnt += 1
            ans.append(cnt)
    for a in ans:
        print(a)


if __name__ == '__main__':
    main()