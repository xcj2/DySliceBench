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

s = inp()

n = len(s)

a = s[:((n-1)//2)]
b = s[((n+3)//2)-1:]

for i in range(n//2):
    if s[i] != s[n-1-i]:
        print("No")
        exit()

for j in range((len(a))//2):
    if a[j] != a[len(a)-1-j]:
        print("No")
        exit()

for k in range((len(b))//2):
    if b[k] != b[len(b)-1-k]:
        print("No")
        exit()

print("Yes")