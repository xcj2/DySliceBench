import sys
from collections import defaultdict

sys.setrecursionlimit(500000)

class Fraction:
    def gcd(self, a ,b):
        a,b = max(a,b),min(a,b)
        while a%b!=0:
            a,b = b,a%b
        return b

    def frac(self,a,b):
        if a==0 and b==0:
            return (0,0)
        elif a==0:
            return (0,1)
        elif b==0:
            return (1,0)
        else:
            d = self.gcd(abs(a),abs(b))
            if a<0:
                a = -a
                b = -b
            return (a//d,b//d)
    
    def __init__(self, a, b):
        self.value = self.frac(a,b)

    def v(self):
        return self.value

    def __lt__(self, other):
        assert self.value!=(0,0) and other.value!=(0,0), 'value (0,0) cannot be compared.'
        a,b = self.value
        c,d = other.value
        return a*d < b*c
    
    def __le__(self, other):
        assert self.value!=(0,0) and other.value!=(0,0), 'value (0,0) cannot be compared.'
        a,b = self.value
        c,d = other.value
        return a*d <= b*c

    def __eq__(self, other):
        a,b = self.value
        c,d = other.value
        return a==c and b==d

    def __ne__(self, other):
        a,b = self.value
        c,d = other.value
        return not (a==c and b==d)

    def __gt__(self, other):
        assert self.value!=(0,0) and other.value!=(0,0), 'value (0,0) cannot be compared.'
        a,b = self.value
        c,d = other.value
        return a*d > b*c

    def __ge__(self, other):
        assert self.value!=(0,0) and other.value!=(0,0), 'value (0,0) cannot be compared.'
        a,b = self.value
        c,d = other.value
        return a*d >= b*c

    def __add__(self, other):
        a,b = self.value
        c,d = other.value
        return Fraction(a*d + b*c, b*d)
        
    def __sub__(self, other):
        a,b = self.value
        c,d = other.value
        return Fraction(a*d - b*c, b*d)

    def __mul__(self, other):
        a,b = self.value
        c,d = other.value
        return Fraction(a*c, b*d)

    def __truediv__(self, other):
        a,b = self.value
        c,d = other.value
        return Fraction(a*d, b*c)
    
    def __neg__(self):
        a,b = self.value
        return Fraction(-a,b)
        
    def inv(self):
        return Fraction(1,1) / self

def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())

    vec = [list(map(int,input().split())) for i in range(N)]

    arg = defaultdict(int)
    zero = 0
    for v in vec:
        if v[0] == 0 and v[1] == 0:
            zero += 1
        else:
            f = Fraction(v[0],v[1])
            arg[f.v()] += 1
            arg[(-f.inv()).v()] += 0

    pair = []
    fd = lambda : False

    checked_list = defaultdict(fd)
    for key in arg:
        if not checked_list[key]:
            inv = (-Fraction(*key).inv()).v()
            pair.append([arg[key],arg[inv]])
            checked_list[inv] = True

    mod = 1000000007

    ans = 1

    for p1,p2 in pair:
        ans *= pow(2,p1,mod) + pow(2,p2,mod) - 1
        ans %= mod

    ans += zero
    ans %= mod

    print((ans+mod-1)%mod)

if __name__ == '__main__':
    main()



