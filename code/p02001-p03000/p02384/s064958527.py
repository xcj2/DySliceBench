a, b, c, d, e, f = map(int, input().split())

num = int(input())

def dice1(x):
    if x == b:
        return c
    elif x == c:
        return e
    elif x == d:
        return b
    else:
        return d

def dice2(x):
    if x == a:
        return d
    elif x == c:
        return a
    elif x == d:
        return f
    else:
        return c

def dice3(x):
    if x == a:
        return b
    elif x == b:
        return f
    elif x == e:
        return a
    else:
        return e

def dice4(x):
    if x == a:
        return e
    elif x == b:
        return a
    elif x == e:
        return f
    else:
        return b

def dice5(x):
    if x == a:
        return c
    elif x == c:
        return f
    elif x == d:
        return a
    else:
        return d

def dice6(x):
    if x == b:
        return d
    elif x == c:
        return b
    elif x == d:
        return e
    else:
        return c

for i in range(num):
    j, k = map(int, input().split())
    if j == a:
        print(dice1(k))
    elif j == b:
        print(dice2(k))
    elif j == c:
        print(dice3(k))
    elif j == d:
        print(dice4(k))
    elif j == e:
        print(dice5(k))
    else:
        print(dice6(k))


