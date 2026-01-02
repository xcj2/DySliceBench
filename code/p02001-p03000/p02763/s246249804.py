import sys

sys.setrecursionlimit(500000)
def input():
    return sys.stdin.readline()[:-1]

class BIT:
            
    def __init__(self, L):
        self.N = len(L)
        self.bit = [0]*self.N
        #for i,l in enumerate(L):
        #    self.add(i,l)
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
        return x+1


def main():
    #da=BIT([1,2,3])
    #print(da.bit)
    #print(da.sum(0))
    N = int(input())

    B = [BIT([0]*N) for i in range(26)]

    S = list(input())

    for i in range(N):
        B[ord(S[i]) - ord("a")].add(i, 1)

    Q = int(input())

    for i in range(Q):
        a,b,c = input().split()
        if a=="1":
            #print(B[0].bit)
            index = int(b)-1
            c = c
            if not S[index]==c:
                old = ord(S[index]) - ord("a")
                num = ord(c) - ord("a")
                B[num].add(index, 1)
                B[old].add(index, -1)
                S[index] = c
        else:
            #print(B[0].bit)
            #print(B[0].sum(1))
            l = int(b)-1
            r = int(c)-1
            ans = 0
            for j in range(26):
                if l==0:
                    if B[j].sum(r)>0:
                        ans+=1
                else:
                    if B[j].sum(r)-B[j].sum(l-1)>0:
                        ans+=1

            print(ans)

if __name__ == '__main__':
    main()

