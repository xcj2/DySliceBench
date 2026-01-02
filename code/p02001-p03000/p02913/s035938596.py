from collections import deque

base = 10007
mod1 = int(1e9 + 7)
mod2 = int(1e9 + 9)


class RollingHash:
    def __init__(self, s):
        self.s = s
        self.len = len(s)
        self.mod1_table = [pow(base, i, mod1) for i in range(self.len + 2)]
        self.mod2_table = [pow(base, i, mod2) for i in range(self.len + 2)]
        self.inv1_table = [pow(self.mod1_table[i], mod1 - 2, mod1) for i in range(self.len + 2)]
        self.inv2_table = [pow(self.mod2_table[i], mod2 - 2, mod2) for i in range(self.len + 2)]
        self.elm_1 = [0]
        self.elm_2 = [0]
        for i in range(self.len):
            val_1 = self.elm_1[-1] + self.mod1_table[len(self.elm_1)] * ord(s[i])
            val_2 = self.elm_2[-1] + self.mod2_table[len(self.elm_2)] * ord(s[i])
            self.elm_1.append(val_1 % mod1)
            self.elm_2.append(val_2 % mod2)
    
    def get(self, l, r):
        val_1 = (self.elm_1[r] - self.elm_1[l]) * self.inv1_table[l] % mod1
        val_2 = (self.elm_2[r] - self.elm_2[l]) * self.inv2_table[l] % mod2
        return val_1, val_2


def check(s, val):
    que = deque()
    se = set()
    for i in range(s.len - val + 1):
        res = s.get(i, i + val)
        if res in se:
            return True
        que.append(res)
        if len(que) == val:
            se.add(que.popleft())
    
    return False


def main():
    n = int(input())
    s = input()
    rh = RollingHash(s)
    
    
    ok = 0
    ng = n
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(rh, mid):
            ok = mid
        else:
            ng = mid
    
    print(ok)


if __name__ == '__main__':
    main()