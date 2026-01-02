N = int(input())
S = input()


class RollingHash:
    base1 = 1007
    base2 = 2009
    mod1 = 10 ** 9 + 7
    mod2 = 10 ** 9 + 9
    
    def __init__(self, s):
        self.s = s
        
        n = len(s)
        self.hash1 = [0] * (n + 1)
        self.hash2 = [0] * (n + 1)
        self.power1 = [1] * (n + 1)
        self.power2 = [1] * (n + 1)
        for i in range(n):
            self.hash1[i + 1] = (self.hash1[i] * self.base1 + ord(s[i])) % self.mod1
            self.hash2[i + 1] = (self.hash2[i] * self.base2 + ord(s[i])) % self.mod2
            self.power1[i + 1] = (self.power1[i] * self.base1) % self.mod1
            self.power2[i + 1] = (self.power2[i] * self.base2) % self.mod2
            
    def get_hash(self, l, r):
        """Gets hash of S[left:right]"""
        res1 = self.hash1[r] - self.hash1[l] * self.power1[r - l] % self.mod1
        if res1 < 0:
            res1 += self.mod1
        res2 = self.hash2[r] - self.hash2[l] * self.power2[r - l] % self.mod2
        if res2 < 0:
            res2 += self.mod2
            
        return (res1, res2)
    
    def get_lcp(self, a, b):
        """Gets lcp of S[a:] and S[b:]"""
        low = 0
        high = min(len(self.hash1) - a, len(self.hash1) - b)
        
        while high - low > 1:
            mid = (low + high) >> 1
            if self.get_hash(a, a + mid) != self.get_hash(b, b + mid):
                high = mid
            else:
                low = mid
                
        return low


def check(d):
    ctr = {}
    for i in range(N - d + 1):
        p = rh.get_hash(i, i + d)
        if p in ctr:
            if i - ctr[p] >= d:
                return True
        else:
            ctr[p] = i
            
    return False


rh = RollingHash(S)
left = 0
right = N // 2 + 1
while right - left > 1:
    mid = (left + right) >> 1
    if check(mid):
        left = mid
    else:
        right = mid

print(left)
