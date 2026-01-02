import sys
input = sys.stdin.readline

a,b,c,d = map(int,list(input())[:4])


def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def printans(a,b,c,d,op):
    ansstr = str(a)
    ansstr += '+' if op[0] == 0 else '-'
    ansstr += str(b)
    ansstr += '+' if op[1] == 0 else '-'
    ansstr += str(c)
    ansstr += '+' if op[2] == 0 else '-'
    ansstr += str(d)
    ansstr += '=7'

    print(ansstr)

ops = []
for i in range(2):
    for j in range(2):
        for k in range(2):
            ops.append((i, j, k))


for op in ops:
    ans = a
    for i,x in enumerate(op):
        if x == 0:
            if i == 0:
                ans = add(ans, b)
            if i == 1:
                ans = add(ans, c)
            if i == 2:
                ans = add(ans, d)
        else:
            if i == 0:
                ans = sub(ans, b)
            if i == 1:
                ans = sub(ans, c)
            if i == 2:
                ans = sub(ans, d)
    

    if ans == 7:
        printans(a,b,c,d,op)
        break

