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
    N = getInt()
    S = input()
    r, b = 0, 0
    for h in S:
        if h == 'R':
            r += 1
        else:
            b += 1
    d.dmp((r,b),'r,b')
    if r > b:
        return 'Yes'
    else:
        return 'No'


ans = prob()
print(ans)