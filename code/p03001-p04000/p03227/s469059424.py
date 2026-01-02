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
    S = input()
    if len(S) == 2:
        return S
    else:
        return S[-1]+S[-2]+S[-3]
    

ans = prob()
print(ans)