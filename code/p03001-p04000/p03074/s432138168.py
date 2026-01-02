import sys

def i2s():
    return sys.stdin.readline().rstrip()

def ii2ss(n):
    return [sys.stdin.readline() for _ in range(n)]

def sp2nn(sp, sep=' '):
    return [int(s) for s in sp.split(sep)]

def ss2nn(ss):
    return [int(s) for s in list(ss)]

def analyze(S):
    data = []
    i0 = 0
    s0 = S[0]
    sc = 0
    for i, s in enumerate(S):
        if s == s0:
            sc += 1
        else:
            data.append((i0, s0, sc))
            i0 = i
            s0 = s
            sc = 1
    data.append((i0, s0, sc))
    return data

def main(ss):
    N, K = sp2nn(ss[0])
    S = ss[1]
    data = analyze(S)
    cmax = 0
    
    for dl in range(len(data)):
        c = 0
        dw = K * 2
        if data[dl][1] == '1':
            dw += 1
        if dl + dw < len(data):
            c = data[dl+dw][0] - data[dl][0]
        else:
            c = N - data[dl][0]
        if cmax < c:
            cmax = c
    
    print(cmax)
main(ii2ss(2))