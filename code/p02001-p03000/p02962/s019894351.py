# -*- coding: utf-8 -*-
import math
import sys
from collections import defaultdict
buff_readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

INF = 2**60


def gen(a, b, num):
    import random
    result = set()
    while 1:
        while 1:
            v = random.randint(a, b)//2*2+1
            if v not in result:
                break
        for x in range(3, int(math.sqrt(v))+1, 2):
            if v % x == 0:
                break
        else:
            result.add(v)
            if len(result) == num:
                break
    return result


class RH():
    def __init__(self, s, base, mod):
        self.base = base
        self.mod = mod
        self.rev = pow(base, mod-2, mod)

        l = len(s)
        self.h = h = [0]*(l+1)
        tmp = 0
        for i in range(l):
            num = ord(s[i])
            tmp = (tmp*base + num) % mod
            h[i+1] = tmp

        self.pw = pw = [1]*(len(s)+1)
        v = 1
        for i in range(l):
            pw[i+1] = v = v * base % mod

    def calc(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod


class RRH():
    def __init__(self, s, rand=False, num=5):
        if rand:
            bases = gen(2, 10**3, num)
        else:
            bases = {293, 389, 167}

        MOD = 10**9+7
        self.rhs = [RH(s, b, MOD) for b in bases]

    def calc(self, l, r):
        return tuple(rh.calc(l, r) for rh in self.rhs)



class UnionFind():
    def __init__(self):
        self.__table = {}
        self.__size = defaultdict(lambda: 1)
        self.__rank = defaultdict(lambda: 1)

    def __root(self, x):
        if x not in self.__table:
            self.__table[x] = x
        elif x != self.__table[x]:
            self.__table[x] = self.__root(self.__table[x])
        return self.__table[x]

    def same(self, x, y):
        return self.__root(x) == self.__root(y)

    def union(self, x, y):
        x = self.__root(x)
        y = self.__root(y)
        if x == y:
            return False

        if self.__rank[x] < self.__rank[y]:
            self.__table[x] = y
            self.__size[y] += self.__size[x]
        else:
            self.__table[y] = x
            self.__size[x] += self.__size[y]
            if self.__rank[x] == self.__rank[y]:
                self.__rank[x] += 1
        return True

    def size(self, x):
        return self.__size[self.__root(x)]

    def num_of_group(self):
        g = 0
        for k, v in self.__table.items():
            if k == v:
                g += 1
        return g



def slv(S, T):
    lt = len(T)
    ls = len(S)
    SS = S * (-(-lt // ls) * 2 + 1)
    srh = RRH(SS)
    th = RRH(T).calc(0, len(T))

    ok = []
    for i in range(ls+lt):
        if srh.calc(i, i+lt) == th:
            ok.append(i)
    ok = set(ok)
    uf = UnionFind()
    for i in ok:
        if (i + lt) in ok:
            if not uf.union(i, (i+lt) % ls):
                return -1
    ans = 0
    for i in ok:
        ans = max(ans, uf.size(i))
    return ans



def main():
    S = input()
    T = input()
    print(slv(S, T))



if __name__ == '__main__':
    main()
