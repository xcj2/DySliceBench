class Path:
    def __init__(self):
        self.a = -1
        self.b = -1

    def getA(self):
        return self.a
    def setA(self, aa):
        self.a = aa
    def getB(self):
        return self.b
    def setB(self, bb):
        self.b = bb

def trace_path(ps, s, cnt, num):
    res = 0
    
    s2 = []
    ps2 = []
    for i in range(0, len(ps)):
        p = ps[i]
        if p.getA() == s or p.getB() == s:
            s2.append(p)
        else:
            ps2.append(p)
    if len(ps2) == 0:
        if cnt == num:
            res += 1
    else:
        for i in range(0, len(s2)):
            p = s2[i]
            if p.a == s:
                res += trace_path(ps2, p.getB(), cnt+1, num)
            else:
                res += trace_path(ps2, p.getA(), cnt+1, num)
    return res

in1 = input().split()
n = int(in1[0])
m = int(in1[1])

ps = []
for i in range(0, m):
    in2 = input().split()
    p = Path()
    p.a = int(in2[0])
    p.b = int(in2[1])
    ps.append(p)
                       
res = trace_path(ps, 1, 1, n-1)

print(str(res))