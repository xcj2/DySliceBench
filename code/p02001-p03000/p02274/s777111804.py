class BinaryIndexedTree(object):
    __slots__ = ["tree", "size"]

    def __init__(self, size: int):
        self.tree = [0]*(size+1)
        self.size = size+1

    def add(self, index: int, value: int):
        tree = self.tree

        while index < len(tree):
            tree[index] += value
            index += index & -index

    def sum(self, index: int):
        tree, result = self.tree, 0

        while index:
            result += tree[index]
            index -= index & -index

        return result


def solve(A):
    bit = BinaryIndexedTree(len(A)+1)
    ans = 0
    for i, n in enumerate(A):
        ans += i - bit.sum(n-1)
        bit.add(n, 1)

    return ans


if __name__ == "__main__":
    input()
    a = list(map(int, input().split()))
    d = {n: i for i, n in enumerate(sorted(a), start=1)}
    a = [d[n] for n in a]
    print(solve(a))
