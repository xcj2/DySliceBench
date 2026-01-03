# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, A):
    ans = 0
    Ai = [(a, i + 1) for i, a in enumerate(A)]
    Ai.sort(key=lambda x: x[0])
    st = SegmentTree(n=N + 2, f=lambda x, y: x + y)
    st.set_val(0, 1)
    st.set_val(N + 1, 1)
    for a, i in Ai:
        lc = st.query(0, i)
        l = st.bisect_left(lambda x: x < lc)
        r = st.bisect_left(lambda x: x < lc + 1)
        ans += a * (i - l) * (r - i)
        st.set_val(i, 1)
    print(ans)

class SegmentTree:
    def __init__(self, n=None, f=max, identity_factory=int, initial_values=None):
        assert(n or initial_values)
        size = n if n else len(initial_values)
        d = [identity_factory() for _ in range(2 * size + 1)]
        self.__n, self.__d, self.__f, self.__e = size, d, f, identity_factory
        if initial_values:
            for i, v in enumerate(initial_values): d[size + i] = v
            for i in range(size - 1, 0, -1): d[i] = f(d[i << 1], d[i << 1 | 1])

    def get_val(self, index):
        return self.__d[index + self.__n]

    def set_val(self, index, new_value):
        i, d, f = index + self.__n, self.__d, self.__f
        if d[i] == new_value: return
        d[i], i = new_value, i >> 1
        while i:
            d[i], i = f(d[i << 1], d[i << 1 | 1]), i >> 1

    def modify(self, index, value):
        self.set_val(index, self.__f(self.__d[index + self.__n], value))

    def query(self, from_inclusive, to_exclusive):
        ans = self.__e()
        if to_exclusive <= from_inclusive: return ans
        l, r, d, f = from_inclusive + self.__n, to_exclusive + self.__n, self.__d, self.__f
        while l < r:
            if l & 1: ans, l = f(ans, d[l]), l + 1
            if r & 1: ans, r = f(d[r - 1], ans), r - 1
            l, r = l >> 1, r >> 1
        return ans

    def bisect_left(self, func):
        '''func()がFalseになるもっとも左のindexを探す
        '''
        i, j, n, f, d, v = self.__n, self.__n + self.__n, self.__n, self.__f, self.__d, self.__e()
        while i < j:
            if i & 1:
                nv = f(v, d[i])
                if not func(nv): break
                v, i = nv, i + 1
            i, j = i >> 1, j >> 1
        while i < n:
            nv = f(v, d[i << 1])
            if func(nv): v, i = nv, i << 1 | 1
            else: i = i << 1
        return i - n

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    *A, = map(int, input().split())
    main(N, A)
