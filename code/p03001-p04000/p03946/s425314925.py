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
    import sys
    readline = sys.stdin.readline
    # readlines = sys.stdin.readlines
    N, T = map(int, input().split())
    A = list(map(int, readline().split()))

    if N == 2:
        print(1)
        return
    
    L = SegmentTree(A, min, float('inf'))
    R = SegmentTree(A, max, 0)

    profit = 0
    for i in range(1, N + 1):
        l = L.get(0, i + 1)
        r = R.get(i, N + 1)
        profit = max(profit, r - l)
    
    cnt = 0
    for i in range(N):
        l = L.get(0, i + 1)
        r = R.get(i, N + 1)
        if r - l == profit:
            if l == A[i]:
                L.update(i, l - 1)
            else:
                R.update(i, r + 1)
            cnt += 1
    
    print(cnt)


if __name__ == "__main__":
    main()
