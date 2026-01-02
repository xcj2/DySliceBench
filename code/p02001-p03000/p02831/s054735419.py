a,b = list(map(int,input().split()))

class LCM():
    #a、bに最小公倍数または最大公約数を求めたい二つの整数の組を入れる
    def __init__(self,a,b):
        if a < b:a,b = b,a
        self.a = a
        self.b = b

    #最大公約数
    def gcd(self):
        a,b = self.a,self.b
        def nono(a,b):
            if a < b:a,b = b,a
            if a % b == 0:return b
            else:return nono(b,a % b)
        return nono(a,b)

    #最小公倍数
    def lcm(self):
        a,b = self.a,self.b
        def nono(a,b):
            if a < b:a,b = b,a
            if a % b == 0:return b
            else:return nono(b,a % b)
        num = nono(a,b)
        return a*b//num

l = LCM(a,b)

print(l.lcm())