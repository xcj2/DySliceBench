import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

def print_l(l):
    print(' '.join(map(str, l)))

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

s = s_in()
q = n_in()

d = True

pre = []
suf = []

for _ in range(q):
    query = s_in()
    if len(query) == 1:
        d = not d
    else:
        _, f, c = query.split()
        if d:
            if f == '1':
                pre.append(c)
            else:
                suf.append(c)
        else:
            if f == '1':
                suf.append(c)
            else:
                pre.append(c)

s = "".join(pre[::-1]) + s + "".join(suf)

if d:
    print(s)
else:
    print(s[::-1])
