def f2(p):
    return 2*p
def f4(p):
    if p<5:
        return 3*p
    else:
        return 4*p
def f14(p):
    if p==2:
        return 16
    elif p==3:
        return 30
    elif p==5:
        return 60
    elif p==7:
        return 91
    else:
        return 101
def f24(p):
    if p==2:
        return 28
    elif p==3:
        return 54
    elif p==5:
        return 100
    else:
        return 101
def f74(p):
    if p==2:
        return 78
    else:
        return 101
    
P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

N = int(input())
c2=0
c4=0
c14=0
c24=0
c74=0

for p in P:
    if f2(p)<=N:
        c2 += 1
    if f4(p)<=N:
        c4 += 1
    if f14(p)<=N:
        c14 += 1
    if f24(p)<=N:
        c24 += 1
    if f74(p)<=N:
        c74 += 1


ans = 0
ans += (c4*(c4-1)//2)*(c2-2)
ans += c14 * (c4 - 1)
ans += c24 * (c2 - 1)
ans += c74

print(ans)