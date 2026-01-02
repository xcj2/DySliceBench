mask = (1<<64)-1
a = 0
def test(a,i):
    if a>>i & 1:
        print(1)
    else:
        print(0)
def _set(a,i):
    a = a | (1<<i)
    return a
def clear(a,i):
    a = a & ~(1<<i)
    return a
def flip(a,i):
    a = a ^ (1<<i)  
    return a
def _all(a):
    if a & mask == mask:
        print(1)
    else:
        print(0)
def _any(a):
    if a == 0:
        print(0)
    else:
        print(1)
def none(a):
    if a & mask == 0:
        print(1)
    else:
        print(0)
def count(a):
    print(bin(a).count('1'))
q = int(input())
for i in range(q):
    s, *t = map(int, input().split())
    if s == 0:test(a,t[0])
    if s == 1:a = _set(a,t[0])
    if s == 2:a = clear(a,t[0])
    if s == 3:a = flip(a,t[0])
    if s == 4:_all(a)
    if s == 5:_any(a)
    if s == 6:none(a)
    if s == 7:count(a)
    if s == 8:print(a)
