def getInt(): return int(input())
def getIntList(): return [int(x) for x in input().split()]
def zeros(n): return [0]*n
# def zeros(n): return np.zeros(n, dtype=np.longlong)
def zeros2(n, m): return [zeros(m) for i in range(n)] # obsoleted zeros((n, m))で代替

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
    N = int(input())
    xport = zeros(5)
    for i in range(5):
        xport[i] = int(input())
    d.dmp((xport),'xport')
    minCapa = INF
    for i in range(5):
        minCapa = min(minCapa, xport[i])
    d.dmp((minCapa),'minCapa')
    minutes = 4
    minutes += (N+minCapa-1)//minCapa
    d.dmp((minutes),'minutes')
    return minutes
    

ans = prob()
print(ans)
