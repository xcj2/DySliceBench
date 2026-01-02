def fi(i, x):
    a, b = lines[i]
    return a*x+b

def find(x):
    def f(i):
        return fi(i+1,x) > fi(i,x)
    mn, mx = -1, len(lines)-1
    idx = (mn+mx)//2
    while mx-mn>1:
        if f(idx):
            mx, idx = idx, (mn + idx)//2
            continue
        mn, idx = idx, (mx + idx)//2
    return fi(idx+1, x)

def insert(a, b):
    (e, f) = lines[-1]
    while len(lines)-1:
        (c, d), (e, f) = (e, f), lines[-2]
        if (c-e)*(b-d) < (d-f)*(a-c):
            break
        lines.pop()
    lines.append((a, b))

N, C = map(int, input().split())
hs = list(map(int, input().split()))
lines = [(-2*hs[0], hs[0]**2)]
for h in hs[1:]:
    r = find(h) + h**2+C
    insert(-2*h, r+h**2)
print(r)
