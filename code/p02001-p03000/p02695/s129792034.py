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

n,m,q=l_in()

abcd=[l_in() for _ in range(q)]

s = []


def check(s):
    return sum(d for a,b,c,d in abcd if s[b-1] - s[a-1] == c)

def search(s, current):
    tmp = 0
    for d in range(current, m+1):
        s.append(d)
        if len(s) == n:
            tmp = max(tmp, check(s))
        else:
            tmp = max(tmp, search(s, d))
        s.pop()
        
    return tmp

print(search(s,1))
