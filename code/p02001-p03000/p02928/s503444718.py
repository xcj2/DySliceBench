class BinaryIndexedTree:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (self.N+1)

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def add(self, i, x):
        while i <= self.N:
            self.bit[i] += x
            i += i & -i

MOD=10**9+7
class Fp(int):
    def __new__(self,x=0):return super().__new__(self,x%MOD)
    def inv(self):return self.__class__(super().__pow__(MOD-2,MOD))
    def __add__(self,value):return self.__class__(super().__add__(value))
    def __sub__(self,value):return self.__class__(super().__sub__(value))
    def __mul__(self,value):return self.__class__(super().__mul__(value))
    def __floordiv__(self,value):return self.__class__(self*self.__class__(value).inv())
    def __pow__(self,value):return self.__class__(super().__pow__(value%(MOD-1), MOD))
    __radd__=__add__
    __rmul__=__mul__
    def __rsub__(self,value):return self.__class__(-super().__sub__(value))
    def __rfloordiv__(self,value):return self.__class__(self.inv()*value)
    def __iadd__(self,value):self=self+value;return self
    def __isub__(self,value):self=self-value;return self
    def __imul__(self,value):self=self*value;return self
    def __ifloordiv__(self,value):self=self //value;return self
    def __ipow__(self,value):self=self**value;return self
    def __neg__(self):return self.__class__(super().__neg__())

N,K,*A=map(int, open(0).read().split())
bit=BinaryIndexedTree(2001)
c=0
for i,a in enumerate(A):
    c+=i-bit.sum(a)
    bit.add(a,1)
d=0
for i,a in enumerate(A):
    d+=N-bit.sum(a)
K=Fp(K)
print(K*c+K*(K-1)//2*d)