def gcd(a,b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a %b)

def gcdlist(l):
    if len(l) == 2:
        return gcd(l[0], l[1])
    f = l.pop()
    s = l.pop()
    m = gcd(f, s)
    l.append(m)
    return gcdlist(l)


def main():
    n, x = map(int, input().split())
    a = [int(v) for v in input().split(' ')]
    a.append(x)
    a.sort()
    dis = [x2 - x1 for x1, x2 in zip(a, a[1:])]
    max_ = 0
    for i in range(n):
        if len(dis) == 1:
            max_ = dis[0]
            break
        try:
            max_ = gcdlist(dis)
        except:
            max_ = 1
    print(max_)

if __name__ == '__main__':
    main()
