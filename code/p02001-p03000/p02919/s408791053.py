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
        # for i in range(len(A)):
        #     self.__node[i + n] = A[i]
        # for i in range(n - 1, 0, -1):
        #     self.__node[i] = self.__dot(self.__node[2 * i], self.__node[2 * i + 1])
    
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
    N = int(input())
    P = map(int, input().split())
    plist = []
    for i, p in enumerate(P):
        plist.append((p, i))
    plist.sort(reverse=True)

    maxSeg = SegmentTree([-1] * N, max, -1)
    minSeg = SegmentTree([N] * N, min, N)

    cnt = 0
    for p, c in plist:
        l2 = maxSeg.get(0, c)
        l1 = -1 if l2 <= 0 else maxSeg.get(0, l2)

        r1 = minSeg.get(c + 1, N)
        r2 = N if r1 >= N - 1 else minSeg.get(r1 + 1, N)

        a = (l2 - l1) * (r1 - c)
        b = (r2 - r1) * (c - l2)
        cnt += p * (a + b)

        maxSeg.update(c, c)
        minSeg.update(c, c)

    print(cnt)


solve()
