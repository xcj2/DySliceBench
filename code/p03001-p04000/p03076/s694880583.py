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
    N = 5
    dish = zeros(N)
    for i in range(N):
        dish[i] = int(input())
    d.dmp((dish),'dish')
    minDigit1 = 10
    idx = N
    time = 0
    for i in range(N):
        if dish[i] % 10 > 0 and minDigit1 > dish[i] % 10:
            idx = i
            minDigit1 = dish[i] % 10
        time += (dish[i]+9)//10*10
        d.dmp((time),'time')
    d.dmp((time),'time')
    d.dmp((idx),'idx')
    if idx < N:
        time -= (dish[idx]+9)//10*10
        time += dish[idx]
    return time
    

ans = prob()
print(ans)
