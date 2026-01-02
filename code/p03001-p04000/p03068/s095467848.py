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
    S = input()
    K = getInt()
    d.dmp((N, S, K),'N, S, K')
    keep = S[K-1]
    newS = ''
    for c in S:
        if c == keep:
            newS += c
        else:
            newS += '*'
    return newS

ans = prob()
print(ans)