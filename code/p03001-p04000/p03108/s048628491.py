# -*- coding: utf-8 -*-


class UnionFind(object):

    def __init__(self, node_count: int):
        self.parent_numbers = [-1 for _ in range(node_count)]

    def find_root(self, node) -> int:
        if self.parent_numbers[node] < 0:
            return node

        self.parent_numbers[node] = self.find_root(self.parent_numbers[node])
        return self.parent_numbers[node]

    def get_group_size(self, node) -> int:
        return -self.parent_numbers[self.find_root(node)]

    def connect(self, node_a, node_b) -> bool:
        a = self.find_root(node_a)
        b = self.find_root(node_b)

        if a == b:
            return False

        if self.get_group_size(a) > self.get_group_size(b):
            self.parent_numbers[a] += self.parent_numbers[b]
            self.parent_numbers[b] = a
        else:
            # swap
            self.parent_numbers[b] += self.parent_numbers[a]
            self.parent_numbers[a] = b
        return True


def main():
    n, m = map(int, input().split())
    ab = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    ans = [0 for _ in range(m)]
    ans[-1] = n * (n - 1) // 2
    uf = UnionFind(n)

    for i in range(m - 1, 0, -1):
        ans[i - 1] = ans[i]
        ai = ab[i][0]
        bi = ab[i][1]

        if uf.find_root(ai) != uf.find_root(bi):
            ans[i - 1] -= uf.get_group_size(ai) * uf.get_group_size(bi)
            uf.connect(ai, bi)

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
