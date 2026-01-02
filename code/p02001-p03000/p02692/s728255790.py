import sys
input = sys.stdin.readline

n, a, b, c = map(int, input().split())
ans = []
ss = []
for _ in range(n):
    ss.append(input().strip())
ss.append('')

def ab():
    global a
    global b
    global c
    ans.append('B')
    a -= 1
    b += 1
def ba():
    global a
    global b
    global c
    ans.append('A')
    a += 1
    b -= 1
def ac():
    global a
    global b
    global c
    ans.append('C')
    a -= 1
    c += 1
def ca():
    global a
    global b
    global c
    ans.append('A')
    a += 1
    c -= 1
def bc():
    global a
    global b
    global c
    ans.append('C')
    b -= 1
    c += 1
def cb():
    global a
    global b
    global c
    ans.append('B')
    b += 1
    c -= 1


for i, s in enumerate(ss):
    if i == n:
        break

    if s == 'AB':
        if a == 0 and b == 0:
            print('No')
            exit()
        elif a == 1 and b == 1:
            nx = ss[i + 1]
            if nx == 'BC':
                ab()
            else:
                ba()
        elif a >= b:
            ab()
        else:
            ba()
    elif s == 'BC':
        if b == 0 and c == 0:
            print('No')
            exit()
        elif b == 1 and c == 1:
            nx = ss[i + 1]
            if nx == 'AC':
                bc()
            else:
                cb()
        elif b >= c:
            bc()
        else:
            cb()
    elif s == 'AC':
        if a == 0 and c == 0:
            print('No')
            exit()
        elif a == 1 and c == 1:
            nx = ss[i + 1]
            if nx == 'AB':
                ca()
            else:
                ac()
        elif a >= c:
            ac()
        else:
            ca()

print('Yes')
for s in ans:
    print(s)
