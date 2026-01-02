from heapq import heappop, heappush


class Medians:
    def __init__(self):
        self.left = []
        self.right = []
        self.size_l = 0
        self.size_r = 0
        self.sum_l = 0
        self.sum_r = 0

    def add(self, n):
        if self.size_l > self.size_r:
            t = -self.left[0]
            if n >= t:
                heappush(self.right, n)
                self.sum_r += n
            else:
                heappop(self.left)
                self.sum_l -= t
                heappush(self.left, -n)
                self.sum_l += n
                heappush(self.right, t)
                self.sum_r += t
            self.size_r += 1
        else:
            if not self.size_l:
                heappush(self.left, -n)
                self.sum_l += n
            else:
                t = self.right[0]
                if n <= t:
                    heappush(self.left, -n)
                    self.sum_l += n
                else:
                    heappop(self.right)
                    self.sum_r -= t
                    heappush(self.right, n)
                    self.sum_r += n
                    heappush(self.left, -t)
                    self.sum_l += t
            self.size_l += 1
    
    def get(self):
        return -self.left[0]


def solve():
    Q = int(input())
    s = 0
    med = Medians()
    for _ in range(Q):
        q, *l, = map(int, input().split())
        if q == 1:
            a, b = l
            s += b
            med.add(a)
        else:
            m = med.get()
            d1 = med.size_l - med.size_r
            d2 = med.sum_r - med.sum_l
            print(m, m*d1+d2+s)


if __name__ == "__main__":
    solve()

    # med = Medians()
    # for i in [4,3,5,1,2,7,9]:
    #     med.add(i)
    #     print(med.get())