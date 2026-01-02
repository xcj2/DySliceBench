p = {
    'm': 1000,
    'c': 100,
    'x': 10,
    'i': 1,
}

def parseNum(s):
    if s[0].isdigit():
        return int(s[0]), s[1:]
    return 1, s

def parseChar(s):
    if s[0] in p:
        return p[s[0]], s[1:]
    print(s)

def parseMCXI(s):
    res = 0
    while s:
        x, s = parseNum(s)
        w, s = parseChar(s)
        res += x * w
    return res

def to(x):
    if x == 0: return None
    if x == 1: return ""
    return str(x)

def toMCXI(x):
    res = ""
    for w, c in sorted(zip(p.values(), p.keys()), reverse=True):
        s = to(x // w)
        if s is not None:
            res += s + c
            x = x % w
    return res
for _ in range(int(input())):
    print(toMCXI(sum(parseMCXI(x) for x in input().split())))