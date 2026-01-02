
#    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
P = [0, 1, 2, 3, 4, 0, 0, 0, 0, 0]
C = [0, 0, 0, 0, 0, 5, 4, 3, 2, 1]
X = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]
import sys
def solve(N):
    N = [int(c) for c in N]
    N = N[::-1]
    p = 0
    b = 0
    s = []
    for i in range(len(N)):
        c = N[i]
        c += b
        if c == 10:
            c = 0
            b = 1
            p += X[c]
            #s.append(P[c])
        elif c == 5:
            if i == len(N)-1:
                p += 5
                #s.append(5)
                b = 0
            else:
                if N[i+1] < 5:
                    p += 5
                    b = 0
                    #s.append(5)
                else:
                    p += 5    
                    b = 1
                    #s.append(0)
        elif c > 5:
            b = 1
            p += X[c]
            #s.append(P[c])
        else:
            b = 0
            p += X[c]
            #s.append(P[c])
    if b:
        s.append(b)
        pass
    #print(b, file=sys.stderr)
    return p + b, s[::-1]

def count(n):
    return sum([int(x) for x in str(n)])

def test(N):
    m = 10e10
    p = 0
    for P in range(N, N*10):
        n = count(P) + count(P - N)
        if n < m:
            p = P
            m = n
    e,s = solve(str(N))
    if e != m:
        print("N=%d"%N, "expected=%d"%m, p, "actual=%d"%e, "".join(str(c) for c in s))

N = [int(x) for x in input()]
a,_ = solve(N)
print(a)
if 1==0:
    for i in range(1, 1000):
        test(i)
    test(159)
    test(149)
    test(449)
    test(959)
    test(949)
    test(939)
    test(539)
    test(569)

