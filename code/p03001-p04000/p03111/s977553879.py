n, A, B, C = (int(i) for i in input().split())
l = [int(input()) for i in range(n)]
a = []
b = []
c = []

def furiwake(x):
    global a
    global b
    global c
    a = []
    b = []
    c = []
    for i in range(1, n+1):
        if dig4(x, i) == 0:
            a.append(l[i-1])
        if dig4(x, i) == 1:
            b.append(l[i-1])
        if dig4(x, i) == 2:
            c.append(l[i-1])

def dig4(n, k):
    return (n%(4**k))//(4**(k-1))

def cost():
    costa = 10 * (len(a)-1) + abs(sum(a)-A)
    costb = 10 * (len(b)-1) + abs(sum(b)-B)
    costc = 10 * (len(c)-1) + abs(sum(c)-C)
    return costa+costb+costc

ans = 1000000000
for i in range(1, 4**8):
    furiwake(i)
    if(len(a)*len(b)*len(c)):
        ans = min(ans, cost())
print(ans)