class RollingHash():
    def __init__(self, s):
        self.length = len(s)
        self.base1 = 1009
        self.base2 = 1007
        self.mod1 = 10**9 + 7
        self.mod2 = 10**9 + 9
        self.hash1 = [0] * (self.length + 1)
        self.hash2 = [0] * (self.length + 1)
        self.pow1 = [1] * (self.length + 1)
        self.pow2 = [1] * (self.length + 1)

        for i in range(self.length):
            self.hash1[i+1] = (self.hash1[i] + ord(s[i])) * self.base1 % self.mod1
            self.hash2[i+1] = (self.hash2[i] + ord(s[i])) * self.base2 % self.mod2
            self.pow1[i+1] = self.pow1[i] * self.base1 % self.mod1
            self.pow2[i+1] = self.pow2[i] * self.base2 % self.mod2
        
    def get(self, l, r):
        t1 = self.hash1[r] - self.hash1[l] * self.pow1[r-l] % self.mod1
        t1 = (t1 + self.mod1) % self.mod1
        t2 = self.hash2[r] - self.hash2[l] * self.pow2[r-l] % self.mod2
        t2 = (t2 + self.mod2) % self.mod2
        return (t1, t2)

class FastRollingHash():
    def __init__(self, s):
        self.length = len(s)
        self.base = 1009
        self.mod = (1 << 61) - 1
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