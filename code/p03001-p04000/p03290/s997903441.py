import sys
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]
d, g = ri_()
p, c = [0] * d, [0] * d
for i in range(d):
    p[i], c[i] = ri_()
ans = 1000
for bit in range(1 << d):
    pro = 0
    poi = 0
    L = []
    for i in range(d):
        if bit & (1 << i):
            pro += p[i]
            poi += p[i] * (i + 1) * 100 + c[i]
        else:
            L.append(i)
    for i in L[::-1]:
        if poi < g:
            tmp = min(p[i], -(-(g - poi) // (100 * (i + 1))))
            pro += tmp
            poi += tmp * 100 * (i + 1)
        else:
            break
    if poi >= g:
        ans = min(ans, pro)
print(ans)