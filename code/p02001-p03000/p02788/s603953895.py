from bisect import bisect_right
import sys
input = sys.stdin.readline

class BIT:
    """ 区間加算BIT(区間加算・区間合計取得) """
 
    def __init__(self, N):
        # 添字0が使えないので、内部的には全て1-indexedとして扱う
        N += 1
        self.N = N
        self.data0 = [0] * N
        self.data1 = [0] * N
 
    def _add(self, data, k, x):
        k += 1
        while k < self.N:
            data[k] += x
            k += k & -k
 
    def _get(self, data, k):
        k += 1
        s = 0
        while k:
            s += data[k]
            k -= k & -k
        return s
 
    def add(self, l, r, x):
        """ 区間[l,r)に値xを追加 """
 
        self._add(self.data0, l, -x*(l-1))
        self._add(self.data0, r, x*(r-1))
        self._add(self.data1, l, x)
        self._add(self.data1, r, -x)
 
    def query(self, l, r):
        """ 区間[l,r)の和を取得 """
 
        return self._get(self.data1, r-1) * (r-1) + self._get(self.data0, r-1) \
             - self._get(self.data1, l-1) * (l-1) - self._get(self.data0, l-1)

def main():
    N, D, A = map(int, input().split())
    B = []

    for i in range(N):
        x, h = map(int, input().split())
        B.append((x,h))

    B.sort()
    X = [0] * N
    H = [0] * N
    for i in range(N):
        X[i], H[i] = B[i]

    bit = BIT(N)
    ans = 0
    for i in range(N):
        H[i] -= bit.query(i, i+1)
        if H[i] <= 0:
            continue
        cnt = H[i] // A if H[i] % A == 0 else H[i] // A + 1
        index = bisect_right(X, X[i] + 2 * D)
        bit.add(i, index, cnt * A)
        ans += cnt

    print(ans)



if __name__ == "__main__":
    main()