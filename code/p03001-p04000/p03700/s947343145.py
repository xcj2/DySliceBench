from bisect import bisect_left
try:
    from collections.abc import Sequence
except:
    from collections import Sequence


class LazySequence(Sequence):
    def __init__(self, f, n):
        self.f = f
        if isinstance(n, int):
            self.r = range(n)
        elif isinstance(n, range):
            self.r = n
        else:
            raise TypeError

    def __len__(self):
        return len(self.r)

    def __getitem__(self, i):
        r = self.r[i]
        if isinstance(r, int):
            return self.f(r)
        else:
            return self.__class__(self.f, r)


N, A, B = map(int, input().split())
D = A - B
H = [int(input()) for _ in range(N)]
H.sort()
l = (H[0] - 1) // A + 1
r = (H[-1] - 1) // B + 1


def isenough(n):
    b = B * n
    for h in H:
        n -= max(0, (h - b - 1) // D + 1)
        if n < 0:
            return False
    return True


a = LazySequence(isenough, r + 1)
ans = bisect_left(a, True, l, r)
print(ans)
