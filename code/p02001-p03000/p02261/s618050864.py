import copy
num =int(input())

l = input().split()

def ccompare( p, q):
    return ord(p[1]) - ord(q[1])


def bsort(l):
    a = copy.copy(l)
    for i in range(len(a)):
        for j in reversed(range(i+1,len(a))):
            if ccompare(a[j],a[j-1]) < 0:
                tmp = a[j-1]
                a[j-1] = a[j]
                a[j] = tmp
    return a
def ssort(l):
    b = copy.copy(l)
    for i in range(len(b)):
        minj = i
        for j in range(i,len(b)):
            if ccompare(b[j], b[minj]) < 0:
                minj = j
        tmp = b[minj]
        b[minj] = b[i]
        b[i] = tmp
    return b
    
def show(lst):
    for i in range(len(lst)):
        print(lst[i], end="")
        if i < len(lst)-1:
            print(" ", end="")
        else:
            print()

def complist(s,t):
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True

bres = bsort(l)
sres = ssort(l)
show(bres)
print("Stable")
show(sres)
if complist(bres, sres):
    print("Stable")
else:
    print("Not stable")

