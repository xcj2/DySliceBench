def inp():
    return input()
def iinp():
    return int(input())
def inps():
    return input().split()
def miinps():
    return map(int,input().split())
def linps():
    return list(input().split())
def lmiinps():
    return list(map(int,input().split()))
def lmiinpsf(n):
    return [list(map(int,input().split()))for _ in range(n)]

n = iinp()
q = lmiinps()

k = 1
l = 0
s = 0

a = sorted(q)
a.append(0)

b = [0]*(a[n-1])
d = [0]*(a[n-1])

for i in range(n):
    if a[i] == a[i+1]:
        k += 1
    else:
        l = ((k*(k-1))//2)
        s += l
        b[a[i]-1]=l
        d[a[i]-1]=k
        k = 1

for j in q:
    p = s-((b[j-1])-((b[j-1] *(d[j-1]-2)) // d[j-1]))
    print(p)