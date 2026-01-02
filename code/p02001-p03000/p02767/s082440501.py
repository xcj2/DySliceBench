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
X = l_in()

P1 = sum(X)//N
P2 = sum(X)//N + 1

print(min(sum((P1-x)**2 for x in X), sum((P2-x)**2 for x in X)));
