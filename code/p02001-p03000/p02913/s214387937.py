class RollingHash:
    def __init__(self, s):
        b1, b2 = 1007, 2009
        self.mod1, self.mod2 = 10**9+7, 10**9+9
        self.size = len(s)
        self.string = s

        self.hash1 = self.make_hashtable(b1, self.mod1)
        self.hash2 = self.make_hashtable(b2, self.mod2)
        self.pow1 = self.make_powtable(b1, self.mod1)
        self.pow2 = self.make_powtable(b2, self.mod2)

    def make_hashtable(self, B, MOD):
        hashtable = [0] * (self.size+1)
        for i in range(1, self.size+1):
            hashtable[i] = (hashtable[i-1] * B + ord(self.string[i-1]))%MOD
        return hashtable
    
    def make_powtable(self, B, MOD):
        power = [0] * (self.size+1)
        power[0] = 1
        for i in range(1, self.size+1):
            power[i] = (B * power[i-1])%MOD
        return power

    def get_hash(self, l, length):
        r = length+l-1
        l -= 1
        h1 = (self.hash1[r]-self.hash1[l]*self.pow1[r-l])%self.mod1
        h2 = (self.hash2[r]-self.hash2[l]*self.pow2[r-l])%self.mod2
        return (h1, h2)

from collections import defaultdict

def solve1():
    N = int(input())
    S = input()
    size = len(S)
    hash_table = RollingHash(S)

    ans = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if S[i-1]!=S[j-1]:continue

            left = 1
            right = min(j-i, size-j+1)+1

            while right-left>1:
                m = (left+right)//2
                if hash_table.get_hash(i, m)==hash_table.get_hash(j, m):
                    left = m
                else:
                    right = m
            ans = max(ans, left)

    print(ans)


def solve2():
    N = int(input())
    S = input()
    size = len(S)
    hash_table = RollingHash(S)

    def check(m):
        d = defaultdict(lambda :10**20)
        for i in range(1, size-m+2):
            h = hash_table.get_hash(i, m)
            d[h] = min(d[h], i)
            if (i-d[h])>=m:
                return True
        return False

    left, right = 0, size//2 + 1
    while right-left>1:
        m = (right+left)//2
        if check(m):
            left = m
        else:
            right = m

    print(left)

if __name__ == "__main__":
    # solve1()
    solve2()

