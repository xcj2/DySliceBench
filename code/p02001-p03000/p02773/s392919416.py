from collections import Counter

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
S = []
counter = Counter()

for i in range(N):
    counter[s_in()] += 1


t = counter.most_common()[0][1]
for s in sorted((map(lambda a: a[0], filter(lambda a: a[1] == t,  counter.most_common())))):
    print(s)

