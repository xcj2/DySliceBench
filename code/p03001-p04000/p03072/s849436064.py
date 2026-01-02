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

def prob_1():
    d = Debug()
    d.off()
    S = input()
    d.dmp((S),'S')
    count = 0
    zeroFound = False
    for c in S:
        #d.dmp((c),'c')
        if c == '0':
            zeroFound = True
        elif c == '+':
            if zeroFound:
                zeroFound = False
            else:
                count += 1
        #d.dmp((count),'count')
    if not zeroFound:
        count += 1
    return count

def prob():
    d = Debug()
    d.off()
    N = getInt()
    H = getIntList()
    d.dmp((N,H),'N,H')
    v = zeros(N)
    v[0] = H[0]
    count = 1
    for i in range(N-1):
        if v[i] <= H[i+1]:
            v[i+1] = H[i+1]
            count += 1
        else:
            v[i+1] = v[i]
    d.dmp((v),'v')
    return count


ans = prob()
print(ans)