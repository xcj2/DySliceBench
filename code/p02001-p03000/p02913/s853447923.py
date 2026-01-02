class RollingHash():
    def __init__(self, s):
        self.length = len(s)
        self.base = 1009
        self.mod = (1 << 127) - 1
        self.hash = [0] * (self.length + 1)
        self.pow = [1] * (self.length + 1)
 
        for i in range(self.length):
            self.hash[i+1] = (self.hash[i] + ord(s[i])) * self.base % self.mod
            self.pow[i+1] = self.pow[i] * self.base % self.mod
 
    def get(self, l, r):
        t = self.hash[r] - self.hash[l] * self.pow[r-l] % self.mod
        t = (t + self.mod) % self.mod
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