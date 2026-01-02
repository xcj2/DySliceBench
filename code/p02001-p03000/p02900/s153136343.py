a, b = map(int, input().split())

def gcd(x, y):
    if x < y:
        x, y = y, x
    if x % y == 0:
        return y
    else:
        return gcd(y, x%y)

def prime(n):
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    else:
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return i
        return n

def div(n):
    divs = []
    tmp = n
    while True:
        if tmp == 1:
            return divs
        ret = prime(tmp)
        if ret != 0:
            divs.append(ret)
            tmp = tmp // ret
        else:
            divs.append(ret)
            break

g = gcd(a, b)
print(len(set(div(g)))+1)