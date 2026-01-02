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

n = s_in()
k = n_in()

res = 0
d = len(n)

def comb(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b == 2:
        return a*(a-1)//2
    if b == 3:
        return (a)*(a-1)*(a-2)//6

    return 0
    

# 手前まで完全一致でii桁以降でl回非ゼロの時の場合の数
def calc(i, l):
    m = int(n[i])

    if i == d-1:
        if l == 0:
            if m == 0:
                return 1
            else:
                return 0
        elif l == 1:
            if m == 0:
                return 0
            else:
                return m
        else:
            return 0
            
        
    if m == 0:
        return calc(i+1, l)
    else:
        tmp = calc(i+1, l-1) # i桁めがmの場合
        tmp += (m-1)*comb(d-i-1, l-1)*int(9**(l-1)) # 1..(m-1)
        tmp += comb(d-i-1,l)*int(9**l)

        return tmp

print(calc(0,k))

