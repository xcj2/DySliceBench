N = int(input())
P = list(map(int,input().split()))

D = [0]*N

for i in range(N):
    D[P[i]-1] = i

class BIT:
            
    def __init__(self, L):
        self.N = len(L)
        self.bit = [0]*self.N
        for i,l in enumerate(L):
            self.add(i,l)
        self.N0 = 1
        while self.N0*2 <= self.N:
            self.N0 *= 2

    def add(self, a, w):
        x = a + 1
        for i in range(1000):
            self.bit[x-1] += w
            x += x & -x
            if x > self.N:
                break

    def sum(self, a):
        x = a+1
        ret = 0
        for i in range(1000):
            ret += self.bit[x-1]
            x -= x & -x
            if x <= 0:
                break        
        return ret

    #you can use this function when the BIT has only non-negative values.
    def lower_bound(self, w):
        if w<=0:
            return 0
        x = 0
        k = self.N0
        while k>0:
            if x+k<=self.N:
                if self.bit[x+k-1]<w:
                    w-=self.bit[x+k-1]
                    x+=k
            k//=2
        return x

bit = BIT([0]*N)

def calc_num(x,l1,l2,h1,h2):
    A = (l1-l2)*(h1-x)
    B = (h2-h1)*(x-l1)
    return A+B

ans = 0

for i in range(N):
    j = N-i-1
    bit.add(D[j],1)
    s = bit.sum(D[j])
    if s==i+1:
        h1=h2=N
    elif s==i:
        h2=N
        h1 = bit.lower_bound(s+1)
    else:
        h1 = bit.lower_bound(s+1)
        h2 = bit.lower_bound(s+2)
    if s==1:
        l1=l2=-1
    elif s==2:
        l1 = bit.lower_bound(s-1)
        l2 = -1
    else:
        l1 = bit.lower_bound(s-1)
        l2 = bit.lower_bound(s-2)

    #print(D[j],l1,l2,h1,h2)
    #print(calc_num(D[j],l1,l2,h1,h2))
    ans += calc_num(D[j],l1,l2,h1,h2)*(j+1)

print(ans)