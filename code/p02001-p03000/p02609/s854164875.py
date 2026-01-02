from functools import lru_cache


a = int(input())
b = input()
X = b.count("1")
ans1 = []
ans2 = []

@lru_cache(maxsize=None)
def func1(c):
    x = X + 1
    n = 1
    nsum = 0
    for i in reversed(range(len(c))):
        ans1.append(n)
        nsum += n * int(c[i])
        n = n % x if n > x else n
        n *= 2
    return nsum
    
@lru_cache(maxsize=None)
def func2(c):
    x = X - 1
    if x == 0:
        return 0
    n = 1
    nsum = 0
    for i in reversed(range(len(c))):
        ans2.append(n)
        nsum += n * int(c[i])
        n = n % x if n > x else n
        n *= 2
    return nsum    

def func(c):
    x = c.count("1")
    if x == 0:
        return 0
    n = 1
    nsum = 0
    for i in reversed(range(len(c))):
        nsum += n * int(c[i])
        n = n % x if n > x else n
        if n == 0:
            break
        n *= 2
    nsum %= x
    cans = bin(nsum).count("1")
    if cans == 0:
        return 1
    else:
        return 1 + func(bin(nsum)[2:])
    
allans1 = func1(b)
allans2 = func2(b)
ans1 = ans1[::-1]
if allans2 == 0:
    ans2 = [0] * a
else:
    ans2 = ans2[::-1]

c = list(b)
for i in range(a):
    if c[i] == "0":
        ans = (allans1 + ans1[i]) % (X + 1)
        ans = func(bin(ans)[2:]) + 1
        print(str(ans))
    else:
        if allans2 - ans2[i] == 0 and X - 1 == 0:
            print("0")
        else:
            ans = (allans2 - ans2[i]) % (X - 1)
            ans = func(bin(ans)[2:]) + 1
            print(str(ans))
