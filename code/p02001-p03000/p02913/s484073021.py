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

N = int(input())
S = input()

RH = RollingHash(S)

from collections import defaultdict

def check(length):
    if length==0:
        return True
    dd = defaultdict(int)
    flag = False
    for i in range(N-length+1):
        rh = RH.get(i,i+length)
        if dd[rh]==0:
            dd[rh] = i+1
        else:
            if dd[rh]+length<=i+1:
                flag=True
                break
    return flag

l = 0
r = N

while r-l>1:
    if check((l+r)//2):
        l = (l+r)//2
    else:
        r = (l+r)//2

print(l)