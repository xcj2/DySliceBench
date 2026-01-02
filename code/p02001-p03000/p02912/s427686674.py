import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.buffer.readline


def upsqrt(x):
    k = x ** 0.5
    res = 1
    while res < k:
        res <<= 1
    return res


def botsqrt(x):
    k = x ** 0.5
    res = 1
    while res <= k:
        res <<= 1
    return res >> 1


class VanEmdeBoasTree:
    def __init__(self, size):
        self.universe_size = 1
        while self.universe_size < size:
            self.universe_size <<= 1
        self.minimum = -1
        self.maximum = -1
        self.summary = None
        self.cluster = {}
    
    def __high(self, x):
        return x // botsqrt(self.universe_size)
    
    def __low(self, x):
        return x % botsqrt(self.universe_size)
    
    def __generate_index(self, x, y):
        return x * botsqrt(self.universe_size) + y
    
    def min(self):
        return self.minimum
    
    def max(self):
        return self.maximum
    
    def __empinsert(self, key):
        self.minimum = self.maximum = key
    
    def insert(self, key):
        if self.minimum == -1:
            self.__empinsert(key)
        else:
            if key < self.minimum:
                self.minimum, key = key, self.minimum
            if 2 < self.universe_size:
                if self.__high(key) not in self.cluster:
                    self.cluster[self.__high(key)] = VanEmdeBoasTree(botsqrt(self.universe_size))
                    if self.summary is None:
                        self.summary = VanEmdeBoasTree(upsqrt(self.universe_size))
                    self.summary.insert(self.__high(key))
                    self.cluster[self.__high(key)].__empinsert(self.__low(key))
                else:
                    self.cluster[self.__high(key)].insert(self.__low(key))
            if self.maximum < key:
                self.maximum = key
    
    def is_member(self, key):
        if self.minimum == key or self.maximum == key:
            return True
        elif self.universe_size == 2:
            return False
        else:
            if self.__high(key) in self.cluster:
                return self.cluster[self.__high(key)].is_member(self.__low(key))
            else:
                return False
    
    def successor(self, key):
        if self.universe_size == 2:
            if key == 0 and self.maximum == 1:
                return 1
            else:
                return -1
        elif self.minimum != -1 and key < self.minimum:
            return self.minimum
        else:
            max_incluster = -1
            if self.__high(key) in self.cluster:
                max_incluster = self.cluster[self.__high(key)].max()
            if max_incluster != -1 and self.__low(key) < max_incluster:
                offset = self.cluster[self.__high(key)].successor(self.__low(key))
                return self.__generate_index(self.__high(key), offset)
            else:
                succ_cluster = self.summary.successor(self.__high(key))
                if succ_cluster == -1:
                    return -1
                else:
                    offset = self.cluster[succ_cluster].min()
                    return self.__generate_index(succ_cluster, offset)
    
    def predecessor(self, key):
        if self.universe_size == 2:
            if key == 1 and self.minimum == 0:
                return 0
            else:
                return -1
        elif self.maximum != -1 and self.maximum < key:
            return self.maximum
        else:
            min_incluster = -1
            if self.__high(key) in self.cluster:
                min_incluster = self.cluster[self.__high(key)].min()
            if min_incluster != -1 and min_incluster < self.__low(key):
                offset = self.cluster[self.__high(key)].predecessor(self.__low(key))
                return self.__generate_index(self.__high(key), offset)
            else:
                pred_cluster = -1
                if self.summary is not None:
                    pred_cluster = self.summary.predecessor(self.__high(key))
                if pred_cluster == -1:
                    if self.minimum != -1 and self.minimum < key:
                        return self.minimum
                    else:
                        return -1
                else:
                    offset = self.cluster[pred_cluster].max()
                    return self.__generate_index(pred_cluster, offset)
    
    def delete(self, key):
        if self.minimum == self.maximum:
            self.minimum = self.maximum = -1
            return True
        elif self.universe_size == 2:
            if key == 0:
                self.minimum = 1
            else:
                self.minimum = 0
            self.maximum = self.minimum
            return False
        else:
            if key == self.minimum:
                first_cluster = self.summary.min()
                key = self.__generate_index(first_cluster, self.cluster[first_cluster].min())
                self.minimum = key
            flg0 = self.cluster[self.__high(key)].delete(self.__low(key))
            if flg0:
                del self.cluster[self.__high(key)]
                flg1 = self.summary.delete(self.__high(key))
                if key == self.maximum:
                    if flg1:
                        self.maximum = self.minimum
                    else:
                        max_insummary = self.summary.max()
                        self.maximum = self.__generate_index(max_insummary, self.cluster[max_insummary].max())
            elif key == self.maximum:
                self.maximum = self.__generate_index(self.__high(key), self.cluster[self.__high(key)].max())


def solve():
    N, M = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    veb = VanEmdeBoasTree(10 ** 9)
    for ai in A:
        veb.insert(ai)
    
    counter = Counter(A)
    for _ in range(M):
        maximum = veb.max()
        counter[maximum] -= 1
        if counter[maximum] == 0:
            veb.delete(maximum)
        if counter[maximum // 2] == 0:
            veb.insert(maximum // 2)
        counter[maximum // 2] += 1
    
    ans = 0
    for key, val in counter.items():
        ans += key * val
    print(ans)


if __name__ == '__main__':
    solve()
