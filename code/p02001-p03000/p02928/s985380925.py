import sys
def main():
    input = sys.stdin.readline
    N,K = map(int, input().split())
    A = list(map(int, input().split()))

    #A内での転倒数t1
    bit = BinaryIndexedTree(2001)
    t1 = Mint()
    for i,a in enumerate(reversed(A)):
        t1 += bit.query(a-1)
        bit.add(a,1)
    
    #ひとつ左のAへの転倒数t2
    t2 = Mint()
    for a in A:
        t2 += bit.query(a-1)

    K2 = K * (K - 1) // 2
    ans = t1 * K + t2 * K2
    print(ans)

class BinaryIndexedTree:
    def __init__(self, n=None, f=lambda x,y:x+y, zero=0, initial_values=None):
        assert(n or initial_values)
        self.__f, self.__z, = f, zero
        self.__n = n if n else len(initial_values)
        self.__dat = [zero] * (self.__n + 1)
        if initial_values:
            for i in range(1, self.__n + 1): self.add(i, initial_values[i-1]) #slow

    def add(self, i, v):
        i += 1
        while i <= self.__n:
            self.__dat[i] = self.__f(self.__dat[i], v)
            i += -i&i

    def query(self, r):
        r += 1
        ans = self.__z
        while r:
            ans = self.__f(ans, self.__dat[r])
            r -= -r&r
        return ans
    
class Mint:
    def __init__(self, value=0, mod=10**9+7):
        self.value = ((value % mod) + mod) % mod
        self.mod = mod

    @staticmethod
    def get_value(x): return x.value if isinstance(x, Mint) else x

    def inverse(self):
        a, b = self.value, self.mod
        u, v = 1, 0
        while b:
            t = a // b
            b, a = a - t * b, b
            v, u = u - t * v, v
        return (u + self.mod) % self.mod

    def __repr__(self): return str(self.value)
    def __eq__(self, other): return self.value == other.value
    def __neg__(self): return Mint(-self.value, self.mod)
    def __hash__(self): return hash(self.value)
    def __bool__(self): return self.value != 0

    def __iadd__(self, other):
        self.value = (self.value + Mint.get_value(other)) % self.mod
        return self
    def __add__(self, other):
        new_obj = Mint(self.value, self.mod)
        new_obj += other
        return new_obj
    __radd__ = __add__

    def __isub__(self, other):
        self.value = (self.value - Mint.get_value(other) + self.mod) % self.mod
        return self
    def __sub__(self, other):
        new_obj = Mint(self.value, self.mod)
        new_obj -= other
        return new_obj
    def __rsub__(self, other):
        new_obj = Mint(Mint.get_value(other), self.mod)
        new_obj -= self
        return new_obj

    def __imul__(self, other):
        self.value = self.value * Mint.get_value(other) % self.mod
        return self
    def __mul__(self, other):
        new_obj = Mint(self.value, self.mod)
        new_obj *= other
        return new_obj
    __rmul__ = __mul__

    def __ifloordiv__(self, other):
        other = other if isinstance(other, Mint) else Mint(other, self.mod)
        self *= other.inverse
        return self
    def __floordiv__(self, other):
        new_obj = Mint(self.value, self.mod)
        new_obj //= other
        return new_obj
    def __rfloordiv__(self, other):
        new_obj = Mint(Mint.get_value(other), self.mod)
        new_obj //= self
        return new_obj

if __name__ == '__main__':
    main()