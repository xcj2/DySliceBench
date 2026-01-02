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

n,k,c = l_in()
S = s_in()


i = 0
left = set()

while i < n:
    if S[i] == 'o':
        left.add(i)
        i += 1+c
    else:
        i += 1

i = n-1
right = set()

while i >= 0:
    if S[i] == 'o':
        right.add(i)
        i -= 1+c
    else:
        i -= 1

if len(left) == k and len(right) == k:
    for i in sorted(list(left.intersection(right))):
        print(i+1)

