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

def prob():  # 例題も解けない
    d = Debug()
    d.off()
    N = 6
    dist = zeros(N)
    for i in range(6):
        dist[i] = int(input())
    d.dmp((dist),'dist')
    K = dist[5]
    d.dmp((K),'K')
    for i in range(4):
        if dist[i+1]-dist[i] > K:
            return ':('
    if dist[4]-dist[0] > K:
        return ':('
    return 'Yay!'
    

ans = prob()
print(ans)
