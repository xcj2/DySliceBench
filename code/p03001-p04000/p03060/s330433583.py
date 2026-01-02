def getInt(): return int(input())
def getIntList(): return [int(x) for x in input().split()]
def zeros(n): return [0]*n

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
    N = getInt()
    V = getIntList()
    C = getIntList()
    d.dmp((N),'N')
    d.dmp((V),'V')
    d.dmp((C),'C')
    smMarg = 0
    for i in range(N):
        marg = V[i]-C[i]
        if marg > 0:
            smMarg += marg
            #d.dmp((i,marg,smMarg),'(i,marg,smMarg)')
    return smMarg

ans = prob()
print(ans)