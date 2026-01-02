import typing

def _ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n:
        x += 1
    return x

class SegTree:
    '''
    op: 結合律が成り立つ演算
    e: 単位元 A op e = A and e op A = A が成り立つe
    足し算の場合 0, 掛け算の場合 1
    '''
    def __init__(self,
                op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                e: typing.Any,
                v: typing.Union[int, typing.List[typing.Any]]
                ) -> None:
        
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v
        
        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)
    
    def set(self, p: int, x: typing.Any) -> None:
        """
        d[p]にxを代入
        d[p]が変更された分を他の部分に反映する
        O(logn)
        """
        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)
    
    def get(self, p: int) -> typing.Any:
        """
        d[p]を返す
        O(1)
        """
        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: int) -> typing.Any:
        """
        op(d[left],・・・,d[right-1])を返す
        O(logn)
        """
        assert 0 <= left <= right <= self._n
        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        """
        op(d[0],・・・,d[n-1])を返す
        O(1)
        """
        return self._d[1]
    
    def max_right(self,
                left: int,
                f: typing.Callable[[typing.Any], bool]
                ) -> int:
        """
        fが単調とすれば、f(op(d[left],・・・,d[right-1])) = true
        となる最大のrightを求められる
        O(logn)
        """
        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n
        
        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self,
                right: int,
                f: typing.Callable[[typing.Any], bool]
                ) -> int:
        """
        fが単調とすれば、f(op(d[left],・・・,d[right-1])) = true
        となる最小のleftを求められる
        O(logn)
        """

        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0
        
        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)
        
        return 0
    
    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])



def main():
    N: int
    K: int
    A: list
    MAX_A: int = 300005
    N, K = map(int, input().split())
    A = list(int(input()) for _ in range(N))
    seg = SegTree(max,0,MAX_A)
    for i in range(N):
        x: int = A[i]
        left = max(0, A[i] - K)
        right = min(MAX_A, A[i] + K + 1)
        now = seg.prod(left, right) + 1
        seg.set(x, max(now, seg.get(x)))

    print(seg.all_prod())

if __name__ == "__main__":
    main()