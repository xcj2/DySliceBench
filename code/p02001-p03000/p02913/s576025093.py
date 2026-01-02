class RollingHash():
    def __init__(self, string):
        self.n = len(string)
        self.BASE = 1234
        self.MOD = (1 << 61) - 1
        self.hash = [0] * (self.n + 1)
        self.pow = [1] * (self.n + 1)
        
        for i, char in enumerate(string):
            self.hash[i+1] = (self.hash[i] + ord(char)) * self.BASE % self.MOD
            self.pow[i+1] = (self.pow[i] * self.BASE) % self.MOD
            
    def get_hash(self, l, r):
        res = (self.hash[r] - self.hash[l] * self.pow[r-l]) % self.MOD
        return res

n = int(input())
s = input()

rh = RollingHash(s)

ans = 0
def solve(mid):
    length = mid
    set_ = set()
    for l in range(n):
        # [l, l + length), [l + length, l + 2*length)
        if l + 2*length > n:
            break
        set_.add(rh.get_hash(l, l + length))
        tmp = rh.get_hash(l + length, l + 2*length)
        if tmp in set_:
            ans = length
            return True
    return False
  
ok = 0
ng = n//2 + 1
while abs(ng - ok) > 1:
    mid = (ok + ng) // 2
    if solve(mid):
        ok = mid
    else:
        ng = mid
print(ok)
    