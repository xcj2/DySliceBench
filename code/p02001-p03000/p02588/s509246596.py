import sys

readline = sys.stdin.readline
class Bit:
    def __init__(self, lst):
        t = 1
        while (t << 1) <= len(lst):
            for i in range(t, len(lst) - t + 1, t << 1):
                lst[i + t - 1] += lst[i - 1]
            t <<= 1
        self.lst = lst

    def add(self, pos, value):
        pos += 1
        while pos <= len(self.lst):
            self.lst[pos - 1] += value
            pos += pos & (-pos)

    def update(self, pos, value):
        diff = value - self.at(pos)
        self.add(pos, diff)

    def at(self, pos):
        return self.sum(pos + 1) - self.sum(pos)
    
    def sum(self, pos):
        # sum of [0, pos)
        if pos == 0:
            return 0
        s = 0
        while pos > 0:
            s += self.lst[pos - 1]
            #pos -= pos & (-pos)
            pos &= ~(-pos)
        return s
    
def solve():
    N = int(readline())
    A = [float(readline()) for i in range(N)]

    C = [0] * N
    c5s = set()

    for i, a in enumerate(A):
        b = round(a * (10 ** 9))
        c2, c5 = -9, -9
        while b % 2 == 0:
            b //= 2
            c2 += 1
        
        while b % 5 == 0:
            b //= 5
            c5 += 1
        
        C[i] = (c2, c5)
        c5s.add(c5)
        c5s.add(-c5)

    c5_to_i = {c5: i for i, c5 in enumerate(sorted(c5s))}
    
    C.sort()

    c5_comp = [c5_to_i[c5] for c2, c5 in C]
    
    bit = Bit([0] * len(c5_to_i))

    c5_max = max(c5 for c2, c5 in C)


    ans = 0
    j = N - 1
    for i, (c2, c5) in enumerate(C):
        if c2 < 0:
            l, r = i, N
            while l + 1 < r:
                m = (l + r) // 2
                if C[m][0] + c2 >= 0:
                    r = m
                else:
                    l = m
            if r == N:
                continue
            
            while j >= r:
                bit.add(c5_comp[j], 1)
                j -= 1
            
            ans += bit.sum(c5_to_i[c5_max] + 1) - bit.sum(c5_to_i[-c5])
        else:
            while j < i:
                j += 1
                bit.add(c5_comp[j], -1)
            
            while j > i:
                bit.add(c5_comp[j], 1)
                j -= 1

            ans += bit.sum(c5_to_i[c5_max] + 1) - bit.sum(c5_to_i[-c5])
    
    print(ans)


solve()