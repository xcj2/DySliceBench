def f1(c, l):
    for i in range(3):
        if c*3 == l[i]:
            return 1
    return 0

def f2(c, l):
    for i in range(0, 7, 3):
        s = set(h[i:i+3])
        if c in s and len(s) == 1:
            return 1
    return 0

def f3(c, l):
    if c*3 == l[0]+l[4]+l[8]:
        return 1
    if c*3 == l[2]+l[4]+l[6]:
        return 1
    return 0

while True:
    try:
        w = [input() for _ in range(3)]
    except:
        break
    if f1('b', w):
        print('b')
        continue
    if f1('w', w):
        print('w')
        continue
    h = [w[j][i] for i in range(3) for j in range(3)]
    if f2('b', h):
        print('b')
        continue
    if f2('w', h):
        print('w')
        continue
    if f3('b', h):
        print('b')
        continue
    if f3('w' , h):
        print('w')
        continue
    print("NA")