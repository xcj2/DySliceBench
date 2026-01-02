ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))


class saidan:
    def __init__(self,n,cl):
        self.n = n
        self.cl = cl
        self.l = 0
        self.r = n

    def check(self):
        for i in range(self.l,n):
            if cl[i] == 0:
                self.l = i 
                break
        else:
            self.l = self.n-1 


        for i in range(n-self.r,n):
            if cl[self.n-1-i] == 1:
                self.r = self.n-i
                break
            else:
                self.r = 0

        return self.r - self.l

    def swap(self):
        # print('swap', self.l,self.r)
        # print(self.cl)
        cl[self.l], cl[self.r-1] = cl[self.r-1],cl[self.l]

n = ii()
c = input()

cl = []
for i in range(n):
    if c[i] == 'R':
        cl.append(1)
    else:
        cl.append(0)

sd = saidan(n,cl)

ans = 0
while 1:
    if sd.check() <= 1:
        break
    
    sd.swap()
    ans += 1

print(ans)

