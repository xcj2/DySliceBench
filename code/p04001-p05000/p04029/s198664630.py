from itertools import combinations, product


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


def get(fmt):
    ps = input().split()
    r = []
    for p, t in zip(ps, fmt):
        if t == "i":
            r.append(int(p))
        if t == "f":
            r.append(float(p))
        if t == "s":
            r.append(p)
    if len(r) == 1:
        r = r[0]
    return r

def put(*args, **kwargs):
    print(*args, **kwargs)


def rep(n, f, *args, **kwargs):
    return [f(*args, **kwargs) for _ in range(n)]
    
def rep_im(n, v):
    return rep(n, lambda: v)
    
YES_NO = ["NO", "YES"]


N = get("i")

put(N * (N + 1) // 2)
