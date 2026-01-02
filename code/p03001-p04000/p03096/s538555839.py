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

def main():
    N,*C=map(int, open(0).read().split())
    DP=[Fp(1)]*(N+1)
    prev={}
    for i,c in enumerate(C):
        d=DP[i]
        if c in prev and not (i and C[i-1]==c):
            d+=DP[prev[c]]
        prev[c]=i+1
        DP[i+1]=d
    print(DP[N])

if __name__ == "__main__":
    main()