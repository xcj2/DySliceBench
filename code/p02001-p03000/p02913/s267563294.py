class RollingHash():
    def __init__(self, s):
        self.mask30 = (1 << 30) - 1
        self.mask31 = (1 << 31) - 1
        self.length = len(s)
        self.base = 1009
        self.mod = (1 << 61) - 1
        self.hash = [0] * (self.length + 1)
        self.pow = [1] * (self.length + 1)

        for i in range(self.length):
            self.hash[i+1] = self.calcmod(self.mul(self.hash[i], self.base) + ord(s[i]))
            self.pow[i+1] = self.calcmod(self.mul(self.pow[i], self.base))
    
    def mul(self, l, r):
        lu = l >> 31
        ld = l & self.mask31
        ru = r >> 31
        rd = r & self.mask31
        middle = ld * ru + lu * rd
        return ((lu * ru) << 1) + ld * rd + ((middle & self.mask30) << 31) + (middle >> 30)
    
    def calcmod(self, val):
        val = (val & self.mod) + (val >> 61)
        if val > self.mod:
            val -= self.mod
        return val

    def get(self, l, r):
        t = self.calcmod(self.hash[r] - self.mul(self.hash[l], self.pow[r-l]) + self.mod)
        return t

n = int(input())
s = input()
RH = RollingHash(s)

def check(l):
    place = {}
    for i in range(n - l + 1):
        hs = RH.get(i, i + l)
        if hs in place:
            if i - place[hs] >= l:
                return True
        else:
            place[hs] = i
    return False

l = 0; r = n // 2 + 1
while r - l > 1:
    m = (l + r) // 2
    if check(m):
        l = m
    else:
        r = m

print(l)