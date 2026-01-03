
def read():
    return int(input())

def reads(sep=None):
    return list(map(int, input().split(sep)))

def main():
    m = 10**9 + 7
    n = read()
    t = reads()
    a = reads()
    if (t != sorted(t)) or (a != sorted(a, reverse=True)) or (max(t) != max(a)):
        print(0)
        return
    if len([1 for ti,ai in zip(t, a) if ti==ai]) == 0:
        print(0)
        return
    
    b = [0] * n
    o = -1
    for i in range(0, n):
        if o != t[i]:
            b[i] = 1
            o = t[i]
            if a[i] < t[i]:
                print(0)
                return
    o = -1
    for i in range(n-1, -1, -1):
        if o != a[i]:
            b[i] = 1
            o = a[i]
            if t[i] < a[i]:
                print(0)
                return
    r = 1
    for i in range(0, n):
        if b[i] == 0:
            r = (r * min(t[i], a[i])) % m
    print(r)

main()
