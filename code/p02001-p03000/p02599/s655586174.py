import sys
from operator import add


class SegmentTree():
    """
    update, get を提供するSegmentTree

    Attributes
    ----------
    __n : int
        葉の数。2 ^ i - 1
    __dot :
        Segment function
    __e: int
        単位元
    __node: list
        Segment Tree
    """
    def __init__(self, A, dot, e):
        """
        Parameters
        ----------
        A : list
            対象の配列
        dot :
            Segment function
        e : int
            単位元
        """
        n = 2 ** (len(A) - 1).bit_length()
        self.__n = n
        self.__dot = dot
        self.__e = e
        self.__node = [e] * (2 * n)
        for i in range(len(A)):
            self.__node[i + n] = A[i]
        for i in range(n - 1, 0, -1):
            self.__node[i] = self.__dot(self.__node[2 * i], self.__node[2 * i + 1])
    
    def update(self, i, c):
        i += self.__n
        node = self.__node
        node[i] = c
        while i > 1:
            i //= 2
            node[i] = self.__dot(node[2 * i], node[2 * i + 1])

    def get(self, l, r):
        vl, vr = self.__e, self.__e
        l += self.__n
        r += self.__n
        while (l < r):
            if l & 1:
                vl = self.__dot(vl, self.__node[l])
                l += 1
            l //= 2
            if r & 1:
                r -= 1
                vr = self.__dot(vr, self.__node[r])
            r //= 2
        return self.__dot(vl, vr)


def main():
    N, Q = map(int, input().split())
    C = list(map(int, input().split()))

    P = [[] for _ in range(N)]
    for i, c in enumerate(C):
        P[c - 1].append(i)

    right = [0] * N
    for p in P:
        if len(p):
            right[p.pop()] = 1
    seg = SegmentTree(right, add, 0)

    query = [[] for _ in range(N)]
    for i, s in enumerate(sys.stdin.readlines()):
        l, r = map(int, s.split())
        query[r - 1].append((l - 1, i))

    ans = [None] * Q

    cur = N - 1
    for r, q in enumerate(reversed(query)):
        r = (N - 1) - r
        while q:
            l, i = q.pop()
            while r < cur:
                c = C[cur] - 1
                p = P[c]
                if len(p):
                    seg.update(p.pop(), 1)
                cur -= 1
            tmp = seg.get(l, r + 1)
            ans[i] = tmp

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
