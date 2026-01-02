mask = (1<<64)-1
a = 0
def test(a,i):
    if a>>i & 1:
        print(1)
    else:
        print(0)
def _set(a,m):
    a = a | mask[m]
    return a
def clear(a,m):
    a = a & ~mask[m]
    return a
def flip(a,m):
    a = a ^ mask[m]  
    return a
def _all(a,m):
    if a & mask[m] == mask[m]:
        print(1)
    else:
        print(0)
def _any(a,m):
    if a&mask[m] == 0:
        print(0)
    else:
        print(1)
def none(a,m):
    if a & mask[m] == 0:
        print(1)
    else:
        print(0)
def count(a,m):
    print(bin(a&mask[m]).count('1'))
def val(a, m):
    return a & mask[m]
n = int(input())
mask = []
for i in range(n):
    ans = 0
    s, *ma = map(int,input().split())
    for i in ma:
        ans = ans | (1<<i)
    mask += [ans]
q = int(input())
for i in range(q):
    s, *t = map(int, input().split())
    if s == 0:test(a,t[0])
    if s == 1:a = _set(a,t[0])
    if s == 2:a = clear(a,t[0])
    if s == 3:a = flip(a,t[0])
    if s == 4:_all(a,t[0])
    if s == 5:_any(a,t[0])
    if s == 6:none(a, t[0])
    if s == 7:count(a,t[0])
    if s == 8:print(val(a,t[0]))

