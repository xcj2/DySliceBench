

a,b,c,d,e,f = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a//gcd(a, b)*b

def sub(s, c, d):
    # k3*c + k4*d でsに近い値を作る
    k3 = s//c
    k4 = 0
    val = k3 * c + k4 * d
    best = val
    k4 += 1
    while k3>=0:
        val = k3 * c + k4 * d
        if val > s:
            k3 -= 1
        else:
            best = max(val, best)
            k4 += 1
    return best
    
best = (0, 100*a, 0)
k1 = 0
while True:
    k2 = 0
    while True:
        w = 100*k1*a + 100*k2*b
        if w==0:
            k2 += 1
            continue
        if w>f:
            break
        s = min(f - w, int(w*e / 100))
        val = sub(s, c, d)
#         print(s, c, d, val)
        if best[0] < val/(w+val):
            best = (val/(w+val), w, val)
        k2 += 1
    k1+=1
    if 100*k1*a>f:
        break
print(best[1]+best[2], best[2], sep=" ")