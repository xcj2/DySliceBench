from sys import stdin
from operator import itemgetter
readline = stdin.readline


#readline = open('???.txt').readline

VERTICAL_LOW, HORIZONTAL, VERTICAL_HIGH = 0, 1, 2

import math
class segment_tree:
    
    # self.table is 1-indexed
    # math.log2 not implemented 3.2.3
    def __init__(self, size):
        self.offset = 2 ** math.ceil(math.log(size, 2))
        self.table = [0] * self.offset * 2
        for i in reversed(range(1, self.offset)):
            self.table[i] = self.table[2 * i] + self.table[2 * i + 1]

    # [l, r] closed-interval
    def sum(self, l, r):
        return sum(self.__range(l,r))

    def __range(self, l, r):
        l += self.offset
        r += self.offset
        while l <= r:
            if l & 1:
                yield self.table[l]
                l += 1
            l >>= 1
            if r & 1 == 0:
                yield self.table[r]
                r -= 1
            r >>= 1
        
    def add(self, i, x):
        i += self.offset
        self.table[i] += x
        while 1 < i:
            i >>= 1
            self.table[i] = self.table[2 * i] + self.table[2 * i + 1]

def main():
    n = int(readline())
    p = [list(map(int, readline().split())) for _ in range(n)]
    x = set(x1 for x1, y1, x2, y2 in p) | set(x2 for x1, y1, x2, y2 in p)
    c = {xi:i for i, xi in enumerate(sorted(x))}
    que = []
    for x1, y1, x2, y2 in p:
        if y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            que.append((y1, HORIZONTAL, c[x1], c[x2]))
        else:
            if y1 > y2:
                y1, y2 = y2, y1
            x1 = c[x1]
            que.append((y1, VERTICAL_LOW, x1, None))
            que.append((y2, VERTICAL_HIGH, x1, None))
    que.sort(key=itemgetter(0, 1))

    vertical_info = segment_tree(len(x))

    intersection = 0
    for y1, action, x1, x2 in que:
        if action == VERTICAL_LOW:
            vertical_info.add(x1, 1)
        elif action == HORIZONTAL:
            intersection += vertical_info.sum(x1, x2)
        else:
            vertical_info.add(x1, -1)
    print(intersection)
main()