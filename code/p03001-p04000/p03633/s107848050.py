def GCD(a, b):
    if a > b:
        A = a
        B = b
    elif b > a:
        A = b
        B = a
    else:
        return a

    r = A % B
    while r != 0:
        A = B
        B = r
        r = A % B

    return B


def LCM(a, b):
    g = GCD(a, b)
    return a*b // g


def solve(): # ABC070C- Multiple Clocks
    while 1:
        try:
            n = int(input())
            T = []
            for _ in range(n):
                T.append(int(input()))

            l = T[0]
            for i in range(1, n):
                l = LCM(l, T[i])

            print(l)
        except:
            break
            
            
solve()