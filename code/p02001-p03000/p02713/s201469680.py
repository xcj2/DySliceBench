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

n = int(input())
ans = 0
dp = [[[-1 for i in range(201)] for j in range(201)] for k in range(201)]
for i in range(1,n+1):
    for j in range(1,1+n):
        for k in range(1,1+n):
            ls = [i,j,k]
            ls.sort()
            if dp[ls[0]][ls[1]][ls[2]] != -1:
                ans += dp[ls[0]][ls[1]][ls[2]]
                continue
            c = LCM(i,j)
            l = LCM(c.gcd(),k)
            a = l.gcd()
            ans += a
            dp[ls[0]][ls[1]][ls[2]] = a

print(ans)