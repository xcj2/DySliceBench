def getInt(): return int(input())
def getIntList(): return [int(x) for x in input().split()]
def zeros(n): return [0]*n

INF = 10**18

class Debug():
    def __init__(self):
        self.debug = True
 
    def off(self):
        self.debug = False
 
    def dmp(self, x, cmt=''):
        if self.debug:
            if cmt != '':
                w = cmt + ': ' + str(x)
            else:
                w = str(x)
            print(w)
        return x


def prob():
    d = Debug()
    d.off()
    C = zeros(2)
    C[0], C[1], K = getIntList()
    d.dmp((C,K), "C,K")
    for i in range(K):
        n = i % 2
        if C[n] % 2 == 1:
            C[n] -= 1
        C[1-n] += C[n] // 2
        C[n] //= 2
        d.dmp((C,i,n), "C,i,n")
    print(C[0],C[1])

ans = prob()
