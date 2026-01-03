class ModInt:
    def __init__(self, num, mod):
        self.num = num
        self.mod = mod

    def __str__(self):
        return str(self.num)

    def __repr__(self):
        return "ModInt(num: {}, mod: {}".format(self.num, self.mod)

    def __add__(self, other):
        ret = self.num + other.num
        ret %= self.mod
        return ModInt(ret, self.mod)

    def __sub__(self, other):
        ret = self.num - other.num
        ret %= self.mod
        return ModInt(ret, self.mod)

    def __mul__(self, other):
        ret = self.num * other.num
        ret %= self.mod
        return ModInt(ret, self.mod)

    def pow(self, times):
        pw = pow(self.num, times, self.mod)
        return ModInt(pw, self.mod)

    def inverse(self):
        return self.pow(self.mod - 2)

    def __truediv__(self, other):
        num = self * other.inverse()
        return ModInt(num, self.mod)


h, w, a, b = map(int, input().split())
mod = 10 ** 9 + 7

power = [ModInt(1, mod)]
inv = [ModInt(1, mod).inverse()]


def comb(n, r):
    return power[n] * inv[r] * inv[n-r]


for i in range(1, h + w - 1):
    power.append(power[-1] * ModInt(i, mod))
    inv.append(power[-1].inverse())

ans = ModInt(0, mod)
for wi in range(b, w):
    ans += comb(h - a - 1 + wi, wi) * comb(a - 1 + w - wi - 1, a - 1)

print(ans)
