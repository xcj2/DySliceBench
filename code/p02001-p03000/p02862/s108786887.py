ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

class com:
    def __init__(self,max, mod = 1000000007):
        self.fac = [0] * max
        self.inv = [0] * max
        self.finv = [0] * max
        self.mod = mod

        self.fac[0] = self.fac[1] = 1
        self.finv[0] = self.finv[1] = 1
        self.inv[1] = 1

        for i in range(2,max):
            self.fac[i] = self.fac[i-1] * i % mod
            self.inv[i] = mod - self.inv[mod%i] * (mod//i) % mod
            self.finv[i] = self.finv[i-1] * self.inv[i] % mod

    def com(self, n, k):
        if n < k: return 0
        if n < 0 or k < 0: return 0
        return self.fac[n] * (self.finv[k] * self.finv[n - k] % self.mod) % self.mod
    

def main():
    x,y = mi()
    if (x+y) % 3 != 0:
        print(0)
        return

    step = (x+y)//3
    if x < step or y < step:
        print(0)
        return
    
    c = com(step+1)

    ans = c.com(step, x - step)

    print(ans)

main()