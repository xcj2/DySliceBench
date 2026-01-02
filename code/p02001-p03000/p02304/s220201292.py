
import operator
from operator import itemgetter
class SegmentTree:
    # http://tsutaj.hatenablog.com/entry/2017/03/29/204841
    def __init__(self, size, fn=operator.add, default=None, initial_values=None):
        """
        :param int size:
        :param callable fn: 区間に適用する関数。引数を 2 つ取る。min, max, operator.xor など
        :param default:
        :param list initial_values:
        """
        default = default or 0

        # size 以上である最小の 2 冪を size とする
        n = 1
        while n < size:
            n *= 2
        self._size = n
        self._fn = fn

        self._tree = [default] * (self._size * 2 - 1)
        if initial_values:
            i = self._size - 1
            for v in initial_values:
                self._tree[i] = v
                i += 1
            i = self._size - 2
            while i >= 0:
                self._tree[i] = self._fn(self._tree[i * 2 + 1], self._tree[i * 2 + 2])
                i -= 1

    def set(self, i, value):
        """
        i 番目に value を設定
        :param int i:
        :param value:
        :return:
        """
        x = self._size - 1 + i
        self._tree[x] = value

        while x > 0:
            x = (x - 1) // 2
            self._tree[x] = self._fn(self._tree[x * 2 + 1], self._tree[x * 2 + 2])

    def add(self, i, value):
        """
        もとの i 番目と value に fn を適用したものを i 番目に設定
        :param int i:
        :param value:
        :return:
        """
        x = self._size - 1 + i
        self.set(i, self._fn(self._tree[x], value))

    def get(self, from_i, to_i=None, k=0, L=None, r=None):
        """
        [from_i, to_i) に fn を適用した結果を返す
        :param int from_i:
        :param int to_i:
        :param int k: self._tree[k] が、[L, r) に fn を適用した結果を持つ
        :param int L:
        :param int r:
        :return:
        """
        if to_i is None:
            return self._tree[self._size - 1 + from_i]

        L = 0 if L is None else L
        r = self._size if r is None else r

        if from_i <= L and r <= to_i:
            return self._tree[k]

        if to_i <= L or r <= from_i:
            return None

        ret_L = self.get(from_i, to_i, k * 2 + 1, L, (L + r) // 2)
        ret_r = self.get(from_i, to_i, k * 2 + 2, (L + r) // 2, r)
        if ret_L is None:
            return ret_r
        if ret_r is None:
            return ret_L
        return self._fn(ret_L, ret_r)

    def __len__(self):
        return self._size

def resolve():
    BOTTOM, HORIZONTAL, TOP = 0, 1, 2
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    # X軸の点を列挙
    X = set(x1 for x1, y1, x2, y2 in XY) | set(x2 for x1, y1, x2, y2 in XY)
    # X軸の点を左端から順序付け
    c = {xi: i for i, xi in enumerate(sorted(X))}

    que = []
    for x1, y1, x2, y2 in XY:
        if y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            # 高さが同じ場合、左、右に点がある
            que.append((y1, HORIZONTAL, c[x1], c[x2]))
        else:
            if y1 > y2:
                y1, y2 = y2, y1
            x1 = c[x1]
            # 高さが違う場合、X軸は同じでY軸は高いか、低いかで場合分け
            que.append((y1, BOTTOM, x1, None))
            que.append((y2, TOP, x1, None))
    # yを下から走査するためにソート
    que.sort(key=itemgetter(0, 1))

    st = SegmentTree(len(X))
    ans = 0
    for y, action, x1, x2 in que:
        if action == BOTTOM:
            st.add(x1, 1)
        elif action == TOP:
            # 判定が終る線分なので削除
            st.add(x1, -1)
        else:
            # X軸の左右の範囲内にある線分を数える
            ans += st.get(x1, x2+1)
    print(ans)

if __name__ == '__main__':
    resolve()

