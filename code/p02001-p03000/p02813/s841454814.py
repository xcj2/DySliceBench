def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

class Interval():
    def __init__(self, li):
        self.li = li
        self.n = len(li)
        self.sum_li = [li[0]]
        for i in range(1, self.n):
            self.sum_li.append(self.sum_li[i-1] + li[i])

    def sum(self, a, b=None):
        if b is None:
            return self.sum(0, a)

        res = self.sum_li[min(self.n-1, b-1)]
        if a > 0:
            res -= self.sum_li[a-1]
        return res

N = n_in()
P = l_in()
Q = l_in()


kaijo = [1]

[kaijo.append((i+1)*kaijo[i]) for i in range(8)]


i = N-1
res = 0
lis = list(range(1, N+1))
for p in P[:N-1]:
    res += lis.index(p)*kaijo[i]
    lis.remove(p)
    i -= 1;

i = N-1
res2 = 0
lis = list(range(1, N+1))
for p in Q[:N-1]:
    res2 += lis.index(p)*kaijo[i]
    lis.remove(p)
    i -= 1;

print(abs(res-res2))

