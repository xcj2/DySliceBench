import sys
lines = sys.stdin.readlines()
R, C = tuple(int(i) for i in lines[0].split(' '))
lines = ''.join(i.strip() for i in lines[1:])


def doD(cs):
    d = {}
    for c in cs:
        if c not in d: d[c] = 0
        d[c] += 1
    return d

def doAns(b):
    print('Yes' if b else 'No')
    sys.exit(0)

def meme(d, rem, val):
    remc = []
    d2 = {}
    for k,v in d.items():
        count = v % val
        remc += [k]*count
        rem -= count
        d2[k] = v - count
    if rem > 0:
        for k,v in d2.items():
           while v >= val and rem > 0:
               v -= val
               rem -= val
               remc += [k]*val
    return (rem, ''.join(remc))

if R == 1 and C == 1:
    doAns(True)
elif R == 1 or C == 1:
    rem = (R + C + 1)%2
    doAns(meme(doD(lines), rem, 2)[0] == 0)
elif R % 2 == 0 and C % 2 == 0:
    doAns(meme(doD(lines), 0, 4)[0] == 0)

rem = (R%2) * C + (C%2)*R
if R % 2 + C % 2 == 1:
    rem, remc = meme(doD(lines), rem, 4)
    if rem != 0: doAns(False)
    rem, remc = meme(doD(remc), len(remc)%2, 2)
    doAns(rem == 0)
    
if R%2 and C%2:
    rem -= 1
    rem, remc = meme(doD(lines), rem, 4)
    if rem != 0: doAns(False)
    rem, remc = meme(doD(remc), C-(R+1)%2, 2)    
    if rem != 0: doAns(False)
    rem, remc = meme(doD(remc), C%2, 2)
    doAns(rem == 0)
