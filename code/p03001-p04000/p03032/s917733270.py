from collections import deque, _heapq
N, K = map(int, input().split())
V = deque(map(int, input().split()))

class Money:
    def __init__(self):
        self.yen = 0
        self.red = []

    def value(self):
        return self.yen + sum(self.red)

    def add(self, yen):
        if yen >= 0:
            self.yen += yen
        else:
            self.red.append(yen)

    def remove(self, yen):
        if yen >= 0:
            self.yen -= yen
        else:
            self.red.remove(yen)

#mny = Money()
def get(cnt, mny, lstop, rstop):
    ans = mny.value()

    if cnt <= 0:
        return ans

    if len(V) > 0:

        if lstop == 0:
            w = V.popleft()
            mny.add(w)
            ans = max(ans, get(cnt-1, mny, lstop, rstop))
            mny.remove(w)
            V.appendleft(w)
        elif lstop > 0:
            lstop -= 1

        if rstop == 0:
            w = V.pop()
            mny.add(w)
            ans = max(ans, get(cnt-1, mny, -1, rstop))
            mny.remove(w)
            V.append(w)

    if len(mny.red) > 0:
        w = min(mny.red)
        mny.red.remove(w)

        V.appendleft(w)
        ans = max(ans, get(cnt-1, mny, -1, -1))
        V.popleft()

        mny.red.append(w)    

    return ans

print(get(K, Money(), 0, 0))
