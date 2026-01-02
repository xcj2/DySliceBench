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

n = n_in()
s = s_in()


from collections import Counter

c=Counter(s)

res = c['R']*c['G']*c['B']


for i in range(n):
    d = 1
    while i+d+d < n:
        if s[i] != s[i+d] and s[i+d] != s[i+d+d] and s[i] != s[i+d+d]:
            res -= 1

        d += 1
    

print(res)
