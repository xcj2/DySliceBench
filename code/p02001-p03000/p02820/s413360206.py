import sys
sys.setrecursionlimit(10000)
def conv(r,s,p,j):
    if j == 'r':
        return p
    if j == 's':
        return r
    if j == 'p':
        return s
def listint():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a
def perse(t,k,num):
    stri = []
    for i in range(k):
        stri.append([])
    for i in range(num):
        stri[i%k].append(t[i])
    return stri
def main(q):
    i = 0
    ans = 0
    while i < len(q)-1:
        if q[i] == q[i+1]:
            ans = ans + conv(r,s,p,q[i])
            i = i+2
        else:
            ans = ans + conv(r,s,p,q[i])
            i = i+1
    if i == len(q)-1:
        ans = ans + conv(r,s,p,q[i])
    return ans
num,k = listint()
r,s,p = listint()
t = input()
afterperse = perse(t,k,num)
ans = 0
for i in range(k):
    ans = ans + main(afterperse[i])
print(ans)