def fi(i, x):
    a, b = lines[i]
    return a*x+b

def find(x):
    if len(lines) == 1:
        return 0
    def f(i):
        # 0<=i<len(lines)-1
        return fi(i+1,x) > fi(i,x)
    mn, mx = 0, len(lines)-2
    idx = (mn+mx)//2
    if f(mn):
        return 0
    if not f(mx):
        return mx+1
    while mx-mn>1:
        if f(idx):
            mx, idx = idx, (mn + idx)//2
            continue
        mn, idx = idx, (mx + idx)//2
    return idx+1

def remove_lines():
    (x, y) = lines.pop()
    a, b  = x, y
    (e, f) = lines[-1]
    while len(lines)-1:
        (c, d), (e, f) = (e, f), lines[-2]
        if (c-e)*(b-d) < (d-f)*(a-c):
            break
        lines.pop()
    lines.append((x, y))

def insert(a, b):
    lines.append((a, b))
    if len(lines) >= 3:
        remove_lines()

N, C = map(int, input().split())
hs = map(int, input().split())
r = 0
lines = []
for i, h in enumerate(hs):
    if i!= 0:
        r = fi(find(h), h) + h**2+C
    insert(-2*h, r+h**2)
print(r)
