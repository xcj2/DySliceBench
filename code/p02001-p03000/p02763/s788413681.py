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
        while i > 0:
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


def solve():
    import sys
    from operator import add
    N = int(input())
    S = list(input())
    Q = int(input())
    Query = sys.stdin.readlines()

    a = ord('a')
    A = [[0] * N for _ in range(26)]
    for i, s in enumerate(S):
        s = ord(s) - a
        A[s][i] = 1
    seg = [SegmentTree(A[i], add, 0) for i in range(26)]

    for i in range(Q):
        t, x, y = Query[i].split()
        t = int(t)
        x = int(x) - 1
        if t == 1 and S[x] != y:
            c = S[x]
            S[x] = y
            seg[ord(c) - a].update(x, 0)
            seg[ord(y) - a].update(x, 1)
            continue
        elif t == 2:
            y = int(y) - 1
            ans = 0
            for j in range(26):
                ans += (seg[j].get(x, y + 1)) > 0
            print(ans)


solve()
