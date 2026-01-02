def getN():
    return int(input())

def getMN():
    a = input().split()
    b = [int(i) for i in a]
    return b[0],b[1]

def getlist():
    a = input().split()
    b = [int(i) for i in a]
    return b
import bisect

n = getN()
pres = getlist()
needs = getlist()

mores = []
for i in range(len(pres)):
    mores.append(pres[i] - needs[i])

ans = 0
mores.sort(reverse=False)

div = bisect.bisect_left(mores, 0)

ans += div
husoku = -(sum(mores[:div]))

amari = mores[div:]#.sort(reverse=True)
if type(amari) == int:
    amari = [amari]
amari.sort(reverse=True)

if sum(amari) < husoku:
    ans = -1
else:
    if husoku > 0:
        for a in amari:
            ans += 1
            if a >= husoku:
                break
            else:
                husoku -= a

print(ans)

